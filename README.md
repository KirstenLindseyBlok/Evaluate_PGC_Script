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

2. The data is downloaded from https://downloads.pdok.nl/ahn3-downloadpage/. DSM-files are labeled "R_*" and DTM-files are labeled "M_*" This commonality is used to create lists which will be used to make the mosaic rasters.

3. Be patient. This step takes a long time

###**Imagery**

Contains all the infra-red aerial imagery as input

The data is prepped by:
1. creating a mosaic to merge all the images

Notes:
Make sure to change the output_location_ir to the folder matching the workspace environment

##**Step two | Image Classification**

###**Segmentation**

Contains the output of the Imagery preparation as input (mosaic of all infra red imagery)

###**Train Classifier**

###**Inspect Training Samples**

In ArcGIS Pro itself. Doesn't work properly but still creates scores
Re-do with new training samples. Currently they do not overlap completely with the area to be classified

Notes
All training samples should lay withing the raster to be classified
Also, processing can take a really long time!
Make sure to use the correct classification schema. 

###**Classify Raster**

###**Reclassify**

To reclassify the training sample values, the block code is moved a bit to the left despite it being part of the same function
this is due to the fact that it will otherwise not work. the extra space will cause a problem in running of the tool. 
Also, no new dataset will be created in this instance. the reclassed values will be added as a new column to the already 
existing dataset. 

###**Accuracy Assessment**

Update Accuracy Assessment points in Pycharm gives wrong output, whereas it works fine in ArcGIS Pro
Both, with the tool itself as python in ArcGIS Pro). Possibly a bug?

###**Percentage of Garden**

Be sure to safe output table as dbf or save in a geodatabase otherwise the code won't run
