import arcpy
from arcpy import env
from arcpy.sa import *

def Segmentation():
    # Create list of rasters filtered based on their name
    irList = arcpy.ListRasters(wild_card="rgb*")
    print(irList)
    # Set local variables
    in_raster = irList
    spectral_detail = "19.0"
    spatial_detail = "15"
    min_segment_size = "20"

    #Execute Segmentation
    #https://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/segment-mean-shift.htm
    for i in irList:
        print(i)
        image = SegmentMeanShift(i, spectral_detail, spatial_detail, min_segment_size)
        image.save(f"segmented_{i}.tif")

def RemoveExtra():
    # Delete unnecesary files
    removeList = arcpy.ListRasters(wild_card="*SegmentMean*")
    print(removeList)
    arcpy.Delete_management(removeList)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/UpScaling/Data"
    env.overwriteOutput = True
    print("Executing Segmentation")
    Segmentation()
    print("Removing Extra files")
    RemoveExtra()
    print("Segmentation Finished")

if __name__ == "__main__":
    main()