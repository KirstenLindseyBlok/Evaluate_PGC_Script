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
    print("Execute Classification")
    Classifiedraster = ClassifyRaster(in_Raster, in_classifier_definition, in_additional_raster)
    Classifiedraster.save("Classified.tif")
    print("Done")

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    Classify_Raster()

if __name__ == "__main__":
    main()