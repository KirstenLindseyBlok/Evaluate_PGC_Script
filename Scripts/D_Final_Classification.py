import arcpy
from arcpy import env
from arcpy.ia import *

def Reclass_DSTM():
    # Set local variables
    in_raster = "Height_0"
    reclass_field = "VALUE"
    remap = "-100000 0 1;0 0.1 2;0.1 2 3;2 100000 4"
    out_raster = "RC_Height.tif"

    # Execute
    print("Execute Reclassification")
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")
    print("Done")

def Raster_Calc():
    #Set local variables
    in_raster_AHN = "rc_height"
    in_raster_Class = "rc_class"

    #Execute
    #https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm
    out_rc_plus_raster = RasterCalculator([in_raster_Class, in_raster_AHN], ["x", "y"], "x+y")
    out_rc_plus_raster.save("Height_and_Class.tif")

def Reclass_Final_Class():
    #Set local variables
    in_raster = "Height_and_Class.tif"
    reclass_field = "Value"
    remap = "0 12 1;12 13 2;13 20 3;20 22 4;22 23 5;23 30 6;30 32 7;32 40 8;40 50 9"
    #1 = pavement                   #6 = trees
    #2 = low ipervious structures   #7 = other surfaces
    #3 = buildings                  #8 = other structures
    #4 = grass                      #9 = bare
    #5 = bushes
    out_raster = "Final_Classes.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/reclassify.htm
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    print("Reclassifying DSTM")
    Reclass_DSTM()
    print("Executing Raster Calculations")
    # Raster_Calc()
    print("Execute Final Classification")
    Reclass_Final_Class()
    print("Done")

if __name__ == "__main__":
    main()