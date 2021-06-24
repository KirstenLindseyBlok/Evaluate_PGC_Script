import arcpy
from arcpy import env


def infrared():
    # Create list of rasters filtered based on their name
    ir_list = arcpy.ListRasters(wild_card="rgb*")

    # Set local Variables
    input_rasters_ir = ir_list
    output_location_ir = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    raster_dataset_name_with_extension_ir = "Mosaic_ir.tif"

    # Execute
    arcpy.MosaicToNewRaster_management(input_rasters_ir, output_location_ir, raster_dataset_name_with_extension_ir,
                                       number_of_bands="3")


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    env.overwriteOutput = True
    print("Executing IR Imagery Prep")
    infrared()
    print("IR Imagery Prep Finished")


if __name__ == "__main__":
    main()
