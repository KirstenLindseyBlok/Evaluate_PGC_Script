import arcpy
from arcpy import env
from arcpy.sa import *


def segmentation():
    # Set local variables
    in_raster = "Mosaic_ir.tif"
    spectral_detail = "19.0"
    spatial_detail = "15"
    min_segment_size = "20"

    # Execute Segmentation
    # https://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/segment-mean-shift.htm
    image = SegmentMeanShift(in_raster, spectral_detail, spatial_detail, min_segment_size)
    image.save("segmented_ir.tif")


def remove_extra():
    # Delete unnecessary files
    remove_list = arcpy.ListRasters(wild_card="*SegmentMean*")
    print(remove_list)
    arcpy.Delete_management(remove_list)


def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing Segmentation")
    segmentation()
    print("Removing Extra files")
    remove_extra()
    print("Segmentation Finished")


if __name__ == "__main__":
    main()
