from arcpy import env
from arcpy.sa import *


def classify_raster():
    # Set local variables
    in_raster = "segmented_ir.tif"
    in_classifier_definition = "ClassDefinition.ecd"
    in_additional_raster = "Mosaic_ir.tif"

    # Execute
    classifiedraster = ClassifyRaster(in_raster, in_classifier_definition, in_additional_raster)
    classifiedraster.save("Classified.tif")


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    env.overwriteOutput = True
    print("Executing Classification")
    classify_raster()
    print("Classification Finished")


if __name__ == "__main__":
    main()
