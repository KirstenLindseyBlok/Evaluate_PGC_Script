import arcpy
from arcpy import env
from arcpy.ia import *


def reclass_dstm():
    # Set local variables
    in_raster = "Height.tif"
    reclass_field = "VALUE"
    remap = "-100000 0 1;0 0.1 2;0.1 2 3;2 100000 4"
    out_raster = "RC_Height.tif"

    # Execute
    print("Execute Reclassification")
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")
    print("Done")


def raster_calc():
    # Set local variables
    in_raster_ahn = "RC_Height.tif"
    in_raster_class = "RC_Class.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm
    out_rc_plus_raster = RasterCalculator([in_raster_class, in_raster_ahn], ["x", "y"], "x+y")
    out_rc_plus_raster.save("Height_and_Class.tif")


def reclass_final_class():
    # Set local variables
    in_raster = "Height_and_Class.tif"
    reclass_field = "Value"
    remap = "0 12 1;12 13 7;13 20 2;20 22 3;22 23 4;23 30 5;30 32 8;32 40 7;40 42 6;42 50 7"
    out_raster = "Final_Classes.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/reclassify.htm
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Reclassifying DSTM")
    reclass_dstm()
    print("Executing Raster Calculations")
    raster_calc()
    print("Execute Final Classification")
    reclass_final_class()
    print("Done")


if __name__ == "__main__":
    main()
