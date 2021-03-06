# PGC_Project

## **General Notes**

1. Be sure to adjust the file paths in the script accordingly. 
   - the workspace environment found at the bottem of all subscripts
   - the output location of [A_Imagery](Scripts/A_Imagery.py)
2. In case of use of a regular folder, instead of a geo-database, be sure to include all file types for both, input data
   and output data. 

## **Step one | Data Preparation**

This project requires five data inputs:
1. Infrared imagery to be classified
2. Training samples to train the classifier
3. Ground truth samples to assess the accuracy of the classifier
4. Private gardens locations per plot
5. A height map to further enhance the classification

The first, fourth and fifth data inputs herefore mentioned can be created using already freely available data. To make 
this data usable, however, it will have to be prepped. This will be done in the first phase of this project: the data 
preparation phase. In case data from other sources is used, other preparations may be needed. Similarly, it is possible 
that no preparations are needed. The sections below will explain what that data should look like. 

### **Gardens**

Contains two data inputs:
- onbegroeidterrein from the BGT which includes the bgt_fysiek attribute 'erf' meaning private gardens
- percelen from the BKR which includes the plots

The data is prepped by:
1. [selecting](https://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/select-layer-by-attribute.htm) the data with 'erf' as bgt_fysiek attribute in onbegroeidterrein
2. [clipping](https://desktop.arcgis.com/en/arcmap/10.3/tools/analysis-toolbox/clip.htm) the percelen data with the new onbegroeidterrein data such that the gardens are split up by their plot

The end result is a polygon shapefile containing all private garden plots. 

### **Height**

Contains two data inputs:
- DSM
- DTM

The data is prepped by:
1. [filling the voids](https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/elevationvoidfill.htm) in both; DSM and DTM
2. using [raster calculation](https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm) to subtract DTM from DSM

The end result is a raster that shows the height of objects relatively to the ground surface. 

Notes:

1. In case of multiple DSM and DTM rasters, enable the Mosaic to Raster definition first.
As such, do not forget to adjust `in_raster*` accordingly:

from

    in_raster_DTM = "M_38AN2.TIF"
    in_raster_DSM = "R_38AN2.TIF"

to

    in_raster_DTM = "Mosaic_DTM"
    in_raster_DSM = "Mosaic_DSM"

2. The DSM & DTM data can be downloaded [here](https://downloads.pdok.nl/ahn3-downloadpage/). 
   
3. DSM-files are labeled `R_*` and DTM-files are labeled `M_*`. This commonality is used to create lists which will be used to make the mosaic rasters.

4. Be patient. This step takes a long time

### **Imagery**

Contains all the infra-red aerial imagery as input

The data is prepped by:
1. creating a [mosaic](https://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/mosaic-to-new-raster.htm) to merge all the images

Notes:
Make sure to change the [output_location_ir](Scripts/A_Imagery.py#L10) to the folder matching the workspace environment

## **Step two | Image Classification**

The initial image classification is done following three steps:
1. [segmentation](https://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/segment-mean-shift.htm)
2. [classifier training](https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/train-support-vector-machine-classifier.htm)
3. [classification](https://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/classify-raster.htm)

### **Segmentation**

Contains the output of the Imagery preparation as input (mosaic of all infrared imagery) and creates a segmented raster 
image based on the spectral and spatial characteristics of the data. 

It must be said that the results of the set [spectral_detail](Scripts/B_Segmentation.py#L9) and [spatial_detail](Scripts/B_Segmentation.py#L10) as well as the [min_segmented_size](Scripts/B_Segmentation.py#L11) using 
python may vary from the results with the same settings in ArcGIS Pro itself. 

Also, be patient! Segmentation tends to take long af. 

### **Train Classifier**

The classifier is trained using the segmented raster image, and the training samples. The final result is a 
classification definition file (in this instance saved as: [ClassDefinition.ecd](Scripts/B_Train_Classifier.py#L9) which can later be used to classify the
imagery. 

May get a warning that the max number of iterations has been reached. In that instance this process may also be run in 
ArcGIS Pro itself; this will shorten the runtime significantly. Simply open ArcGIS Pro or Arc Mapper and search for 
`train support vector machine classifier` in the geo-processing toolbox and match the input-variables to those found in 
this script.

### **Classify Raster**

In this step, the classification definition created earlier is used to classify the (infra-red) imagery. 

## **Step 3 | Accuracy Assessment**

In order to complete the accuracy assessment a couple of steps will have to be taken:
1. [Reclassify](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/reclassify.htm)  the Classified raster
2. Reclassify the Ground Truth Samples
3. [Create Accuracy Assessment Points](https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/create-accuracy-assessment-points.htm) based on Ground Truth
4. [Update Accuracy Assessment Points](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/update-accuracy-assessment-points.htm) with Classified raster
5. Create and Interpret [Confusion Matrix](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/compute-confusion-matrix.htm)

### **Reclassify**

Starting with the first, the data are reclassified such that only three classes remain, namely: Pervious as 10, 
Impervious as 20, and Other as 30. 

Secondly, the ground truth data was reclassified as well, such that here too three classes remain: Pervious (10),
Impervious (20), and Other (30). Make sure that when the local variables are set for the ground truth reclassification, 
the [code_block](Scripts/C_Reclassification.py#L20) is written starting all the way on the left (so the code_block 
definition should be written without any tabs in front of it); otherwise the tabs will be used in the tool itself as 
well, as it were, which will cause the code not to work.

### **Confusion Matrix**

A stratified random sample of points is used to compare the resulting classified raster with ground truth samples. It 
does this by assigning the classified values as well as the ground truth value of the concerned location to the point. 
The comparison can be clearly analysed and interpreted in the confusion matrix which also shows what a specific class 
tents to be misinterpreted as. Ultimately, one should aim for an accuracy of 1, however scores of 0.8 and up are also 
considered to be significant enough to continue. If not, your training samples should be altered. See the final project 
report for more information about how to read the confusion matrix. 

Note:
Be sure to safe the confusion matrix output table as a dbf or save in a geo-database otherwise the code won't run.

## **Step 4 | Final Classification**

The final classification is completed following a couple of steps and sub-steps:
1. Final classification of whole area
   - Reclassification of height data
   - [Raster calculation](https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm) of initial classified raster and height data
   - Reclassification of final classes
   
2. Results of only the garden plots
   - Transform final classification from [raster to polygon](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/raster-to-polygon.htm)
   - [Extract](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/clip.htm) the garden plots

### **Final Classification**

As mentioned earlier, first the height data will have to be reclassified. In total four categories are created:
- With a height up to 0 metres (value = 1)
- With a height between 0 and 0.1 metres (value = 2)
- With a height between 0.1 and 2 metres (value = 3)
- With a height of 2 metres and higher (value =4)

By adding these new values to the reclassified initial classified data (see step 3 - reclassification), the final 
classes can be identified. The final classes include:

    1 = pavement                 5 = trees
    2 = buildings                6 = other surfaces
    3 = grass                    7 = other structures
    4 = bushes                   8 = bare

### **Classification of Gardens**

As indicated earlier, the final classified raster will first have to be transformed to a polygon. This is done to ensure 
the entire garden will be included in the final results. Secondly, the only thing left to be done is extract the 
garden-plots from the final classified polygon file. 

## **Step 5 | Percentage of Garden**

The percentages per garden-plot are calculated in three steps:
1. [tabular intersection](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/tabulate-intersection.htm)
2. [pivot table](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/pivot-table.htm)
3. [add join](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-join.htm)
   - [delete](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/delete-field.htm) unnecessary columns
   - [add field](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm)
   - [calculate field](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/calculate-field.htm)

### **Tabular Intersection**
Intersects the Garden plots with the classified raster to cross tabulate the area, length, count of the intersecting 
features, and the corresponding percentage of the entire garden plot.

### **Pivot Table**
The issue with the tabular intersection tool is that when a garden contains two separate sections that are classified as
green, it will calculate the percentage of those sections separately, instead of giving the combined percentage of the 
total garden plot that is green. That's where the Pivot Table comes in. This tool is able to reduce redundancy in 
records and flatten one-to-many relationships as illustrated below.

**Input Table**

| ID  | Type | Pivot Field |Value Field |
| --- |:----:| -----------:| ----------:|
| 1   | A    | X1          | 20         |
| 1   | A    | X2          | 21         |
| 2   | A    | X1          | 23         |
| 2   | A    | X2          | 29         |
| 2   | B    | X1          | 80         |
| 2   | B    | X2          | 77         |

**Output Table**

| ID  | Type | X1          | X2         |
| --- |:----:| -----------:| ----------:|
| 1   | A    | 20          | 21         |
| 2   | A    | 23          | 29         |
| 2   | B    | 80          | 77         |

The difference being that in this instance Pivot Field would equal the gridcodes, and the value field would contain the percentages. 

### **Add join**

In order to visualise the percentages used as either impervious, pervious, or other, the pivot table will have to be 
joined with the garden plots shapefile. The garden plot shapefile contains a lot of unnecessary attributes however. To 
keep the data clean and understandable, these attributes were first deleted, before the join was executed. 

The pivot table calculated for each class the percentage of the garden it covered. However, instead of knowing what 
percentage is covered by trees, bushes, grass and bare individually, it is more useful to know what percentage of the 
garden has a pervious cover. Therefore, three new fields were added (namely, impervious, pervious, and other), combining 
the percentages of the classes belonging to those groups using field calculation.

Throughout this entire process, column names change. The list below shows which 
values are linked.

    PivotTable = OID                            PivotTab_1 = FID_
    PivotTab_2 = gridcode1 = pavement           PivotTab_3 = gridcode2 = buildings
    PivotTab_4 = gridcode3 = grass              PivotTab_5 = gridcode4 = bushes
    PivotTab_6 = gridcode5 = trees              PivotTab_7 = gridcode6 = other surfaces
    PivotTab_8 = gridcode7 = other structures   PivotTab_9 = gridcode8 = bare

When the percentages of the pervious group are combined, it thus adds up the values 
of PivotTab4, PivotTab5, PivotTab6, and PivotTab9. 
