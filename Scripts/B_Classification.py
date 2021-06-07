from arcpy import env
from arcpy.sa import *


def classify_raster():
    # Set local variables
    in_raster = "segmented_ir.tif"
    in_classifier_definition = "ClassDefinition.ecd"
    in_additional_raster = "Mosaic_ir.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/train-support-vector-machine-classifier.htm
    classifiedraster = ClassifyRaster(in_raster, in_classifier_definition, in_additional_raster)
    classifiedraster.save("Classified.tif")


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing Classification")
    classify_raster()
    print("Classification Finished")


if __name__ == "__main__":
    main()
