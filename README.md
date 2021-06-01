# PGC_Project

##**General Notes**

1. Be sure to adjust the file paths in the script accordingly. Think of the workspace 
   environments, but also some of the output or input locations.
2. In case of use of a regular folder, instead of a geodatabase, be sure to include 
   all file types for both, input data and output data. 

##**Step one | Data Preparation**

This project requires five data inputs:
1. Infra red imagery to be classified
2. Training samples to train the classifier
3. Ground truth samples to assess the accuracy of the classifier
4. Private gardens locations per plot
5. A height map to further enhance the classification

The first, fourht and fifth data inputs herefore mentioned can be created using 
already freely available data. To make this data useable, however, it will have to be 
prepped. This will be done in the first phase of this project: the data preparation 
phase. In case data from other sources is ues, other preparations may be needed. 
Similarly, it is possible that no preparations are needed. The sections below will 
explain what that data should look like. 

###**Gardens**

Contains two data inputs:
- onbegroeidterrein from the BGT wich includes the bgt_fysiek attribute 'erf' 
  meaning private gardens
- percelen from the BKR which includes the plots

The data is prepped by:
1. selecting the data with 'erf' as bgt_fysiek attribute in onbegroeidterrein
2. clipping the percelen data with the new onbegroeidterrein data such that the 
   gardens are split up by their plot

The end result is a polygon shapefile containing all private garden plots. 

###**Height**

Contains two data inputs:
- DSM
- DTM

The data is prepped by:
1. filling the voids in both; DSM and DTM
2. using raster calculation to substract DTM from DSM

The end result is a raster that shows the hight of objects relatively to the ground 
surface. 

Notes:
In case of multiple DSM and DTM rasters, enable the Mosaic to Raster definition 
first.
As such, do not forget to adjust *in_raster* accordingly:


    in_raster_DTM = "M_38AN2.TIF"
    in_raster_DTM = "Mosaic_DTM"

2. The data is downloaded from https://downloads.pdok.nl/ahn3-downloadpage/. 
   DSM-files are labeled "R_*" and DTM-files are labeled "M_*" This commonality is 
   used to create lists which will be used to make the mosaic rasters.

3. Be patient. This step takes a long time

###**Imagery**

Contains all the infra-red aerial imagery as input

The data is prepped by:
1. creating a mosaic to merge all the images

Notes:
Make sure to change the output_location_ir to the folder matching the workspace 
environment

##**Step two | Image Classification**

The initial image classification is done following three steps:
1. segmentation
2. classifier training
3. classification

###**Segmentation**

Contains the output of the Imagery preparation as input (mosaic of all infra red 
imagery) and creates a segmented raster image based on the spectral and spatial 
characteristics of the data. 

It must be said that the results of the set spectral_detail and spatial_detail as 
well as the min_segmented_size using python may vary from the results with the same
settings in ArcGIS Pro itself. 

Also, be patient! Segmentation tents to take long af. 

###**Train Classifier**

The classifier is trained using the segmented raster image, and the training samples. 
The final result is a classification definition file which can later be used to
classify the imagery. 

May get a warning that the max number of iterations has been reached. In that 
instance this process may also be run in ArcGIS Pro itself. 

###**Classify Raster**

In this step, the classification definition created earlier is used to classify the
(infra red) imagery. 

##**Step 3 | Accuracy Assessment**##

In order to complete the accuracy assessment a couple of steps will 
have to be taken:
1. Reclassify the Classified raster 
2. Reclassify the Ground Truth Samples
3. Create Accuracy Assessment Points based on Ground Truth
4. Update Accuracy Assessment Points with Classified raster
5. Create and Interpret Confusion Matrix

###**Reclassify**

Starting with the first, the data are reclassified such that only four classes 
remain, namely: Impervious as 10, Pervious as 20, Bare as 30, and Other as 40. 
Moreover, make sure that when the local variables are set for the ground truth 
classification, the code_block is written starting all the way on the leftn(so the 
code_block definition should be written without any tabs in front of it); otherwise 
the code won't work. Also, no new dataset will be created in this instance; the 
reclassified values will be added as a new column to the already existing dataset. 
Lastly, it was decided to merge the 'water class' together with the 'other class' as
it caused to many mis-classifications. 

###**Accuracy Assessment**

A stratified random sample of points is used to compare the resulting classified 
raster with ground truth samples. It does this by assigning the classified values
as well as the ground truth value of the concerned location to the point. The 
comparison can be clearly analysed and interpreted in the confusion matrix which 
also shows what a specific class tents to be misinterpreted as. Ultimately, one 
should aim for an accuracy of 1, however scores of 0.8 and up are also considered 
to be significant enough to continue. If not, your training samples should be 
altered. See the final project report for more information about how to read the
confusion matrix. 

Note:
Be sure to safe the confusion matrix output table as a dbf or save in a 
geodatabase otherwise the code won't run.

##**Step 4 | Final Classification**##

##**Step 5 | Percentage of Garden**##


