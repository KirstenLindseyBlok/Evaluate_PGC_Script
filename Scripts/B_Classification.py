import arcpy
from arcpy import env
from arcpy.sa import *

def Classify_Raster():
    # Set local variables
    in_Raster = "segmented_ir.tif"
    in_classifier_definition = "ClassDefinition.ecd"
    in_additional_raster = "Mosaic_ir.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/train-support-vector-machine-classifier.htm
    Classifiedraster = ClassifyRaster(in_Raster, in_classifier_definition, in_additional_raster)
    Classifiedraster.save("Classified.tif")

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing Classification")
    Classify_Raster()
    print("Classification Finished")

if __name__ == "__main__":
    main()