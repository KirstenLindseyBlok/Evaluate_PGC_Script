import arcpy
from arcpy import env


def infrared():
    # Create list of rasters filtered based on their name
    ir_list = arcpy.ListRasters(wild_card="rgb*")

    # Set local Variables
    input_rasters_ir = ir_list
    output_location_ir = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    raster_dataset_name_with_extension_ir = "Mosaic_ir.tif"

    # Execute
    # https://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/mosaic-to-new-raster.htm
    arcpy.MosaicToNewRaster_management(input_rasters_ir, output_location_ir, raster_dataset_name_with_extension_ir,
                                       number_of_bands="3")


def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing IR Imagery Prep")
    infrared()
    print("IR Imagery Prep Finished")


if __name__ == "__main__":
    main()
