import arcpy
from arcpy import env
from arcpy.ia import *

def Reclass_DSTM():
    # Set local variables
    in_raster = "Height.tif"
    reclass_field = "VALUE"
    remap = "-100000 0 1;0 0.1 2;0.1 2 3;2 100000 4"
    out_raster = "RC_Height.tif"

    # Execute
    print("Execute Reclassification")
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")
    print("Done")

def Raster_Calc():
    #Set local variables
    in_raster_AHN = "RC_Height.tif"
    in_raster_Class = "RC_Class.tif"

    #Execute
    #https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm
    out_rc_plus_raster = RasterCalculator([in_raster_Class, in_raster_AHN], ["x", "y"], "x+y")
    out_rc_plus_raster.save("Height_and_Class.tif")

def Reclass_Final_Class():
    #Set local variables
    in_raster = "Height_and_Class.tif"
    reclass_field = "Value"
    remap = "0 12 1;12 13 7;13 20 2;20 22 3;22 23 4;23 30 5;30 32 6;32 40 7;40 50 7"
    #1 = pavement                   #5 = trees
    #2 = buildings                  #6 = other surfaces
    #3 = grass                      #7 = other structures
    #4 = bushes                     #8 = bare
    out_raster = "Final_Classes.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/reclassify.htm
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Reclassifying DSTM")
    Reclass_DSTM()
    print("Executing Raster Calculations")
    Raster_Calc()
    print("Execute Final Classification")
    Reclass_Final_Class()
    print("Done")

if __name__ == "__main__":
    main()