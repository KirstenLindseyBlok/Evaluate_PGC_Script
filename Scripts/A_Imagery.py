import arcpy
from arcpy import env

def IR():
    # Create list of rasters in gdb workspace filtered based on their name
    irList = arcpy.ListRasters(wild_card="rgb*")

    # Set local Variables
    input_Rasters_ir = irList
    output_location_ir = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    raster_dataset_name_with_extension_ir = "Mosaic_ir.tif"

    #Execute
    #https://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/mosaic-to-new-raster.htm
    arcpy.MosaicToNewRaster_management(input_Rasters_ir, output_location_ir, raster_dataset_name_with_extension_ir,
                                       number_of_bands="3")

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    print("Executing IR Imagery Prep")
    IR()
    print("Finished")

if __name__ == "__main__":
    main()