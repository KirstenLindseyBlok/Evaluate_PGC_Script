from arcpy import env
from arcpy.ia import *

# def Mosaic():
#     # Create list of rasters in gdb workspace filtered based on their name
#     DSMList = arcpy.ListRasters(wild_card="R*")
#     DTMList = arcpy.ListRasters(wild_card="M*")
#
#     # Set local Variables
#     input_Rasters_DSM = DSMList
#     input_Rasters_DTM = DTMList
#     output_location = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
#     raster_dataset_name_with_extension_DSM = "Mosaic_DSM.tif"
#     raster_dataset_name_with_extension_DTM = "Mosaic_DTM.tif"
#
#     # Execute
#     # https://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/mosaic-to-new-raster.htm
#     arcpy.MosaicToNewRaster_management(input_Rasters_DSM, output_location, raster_dataset_name_with_extension_DSM,
#                                        number_of_bands="1")
#     arcpy.MosaicToNewRaster_management(input_Rasters_DTM, output_location, raster_dataset_name_with_extension_DTM,
#                                        number_of_bands="1")


def fill_dtm():
    # Define input parameters
    in_raster_dtm = "M_38AN2.tif"
    max_void_width = 0

    # Execute the ElevationVoidFill function
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/elevationvoidfill.htm
    out_raster_dtm = ElevationVoidFill(in_raster_dtm, max_void_width)
    out_raster_dtm.save(f"DTM_NoVoid.tif")
    print("Void Fill DTM Completed")


def fill_dsm():
    # Define input parameters
    in_raster_dsm = "R_38AN2.tif"
    max_void_width = 0

    # Execute the ElevationVoidFill function
    out_raster_dsm = ElevationVoidFill(in_raster_dsm, max_void_width)
    out_raster_dsm.save(f"DSM_NoVoid.tif")
    print("Void Fill DSM Completed")


def height():
    #  Set local variables
    in_raster_dtm = "DTM_NoVoid.tif"
    in_raster_dsm = "DSM_NoVoid.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm
    out_rc_minus_raster = RasterCalculator([in_raster_dsm, in_raster_dtm], ["x", "y"], "x-y", "FirstOf", "FirstOf")
    out_rc_minus_raster.save(f"Height.tif")
    print("Calculating Height Data Completed")


def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    # Execute Prep
    print("Executing Height Prep")
    # Mosaic()
    fill_dtm()
    fill_dsm()
    height()
    print("Height Prep Finished")


if __name__ == "__main__":
    main()
