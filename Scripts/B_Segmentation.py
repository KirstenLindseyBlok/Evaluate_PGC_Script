import arcpy
from arcpy import env
from arcpy.sa import *

def Segmentation():
    # Set local variables
    in_raster = "Mosaic_ir.tif"
    spectral_detail = "19.0"
    spatial_detail = "15"
    min_segment_size = "20"

    #Execute Segmentation
    #https://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/segment-mean-shift.htm
    print("Executing Segmentation of")
    image = SegmentMeanShift(in_raster, spectral_detail, spatial_detail, min_segment_size)
    image.save("segmented_ir.tif")
    print("Done")

def RemoveExtra():
    # Delete unnecesary files
    removeList = arcpy.ListRasters(wild_card="*SegmentMean*")
    print(removeList)
    arcpy.Delete_management(removeList)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    Segmentation()
    RemoveExtra()

if __name__ == "__main__":
    main()