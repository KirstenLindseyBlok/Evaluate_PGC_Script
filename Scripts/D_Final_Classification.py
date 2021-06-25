import arcpy
from arcpy import env
from arcpy.ia import *


def reclass_dstm():
    # Set local variables
    in_raster = "Height.tif"
    reclass_field = "VALUE"
    remap = "-100000 0.1 1;0.1 2 2;2 100000 3"
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
    out_rc_plus_raster = RasterCalculator([in_raster_class, in_raster_ahn], ["x", "y"], "x+y")
    out_rc_plus_raster.save("Height_and_Class.tif")


def reclass_final_class():
    # Set local variables
    in_raster = "Height_and_Class.tif"
    reclass_field = "Value"
    remap = "0 11 1; 11 12 2; 12 20 3; 20 21 4; 21 22 7; 22 30 5; 30 31 6; 31 32 7; 32 40 7"
    out_raster = "Final_Classes.tif"

    # Execute
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    env.overwriteOutput = True
    print("Reclassifying DSTM")
    # reclass_dstm()
    print("Executing Raster Calculations")
    # raster_calc()
    print("Execute Final Classification")
    reclass_final_class()
    print("Done")


if __name__ == "__main__":
    main()
