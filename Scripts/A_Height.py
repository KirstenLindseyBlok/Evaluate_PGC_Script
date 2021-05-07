import arcpy
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

def FillDTM():
    #Define input parameters
    in_raster_DTM = "M_38AN2.TIF"
    max_void_width = 0

    #Execute the ElevationVoidFill function
    #https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/elevationvoidfill.htm
    print("Executing Void Fill DTM")
    out_raster_DTM = ElevationVoidFill(in_raster_DTM, max_void_width)
    out_raster_DTM.save(f"DTM_NoVoid.tif")
    print("Done")

def FillDSM():
    #Define input parameters
    in_raster_DSM = "R_38AN2.TIF"
    max_void_width = 0

    #Execute the ElevationVoidFill function
    print("Executing Void Fill DSM")
    out_raster_DSM = ElevationVoidFill(in_raster_DSM, max_void_width)
    out_raster_DSM.save(f"DSM_NoVoid.tif")
    print("Done")

def Height():
    # Set local variables
    in_raster_DTM = "DTM_NoVoid.tif"
    in_raster_DSM = "DSM_NoVoid.tif"

    #Execute
    #https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/raster-calculator.htm
    out_rc_minus_raster = RasterCalculator([in_raster_DSM, in_raster_DTM], ["x", "y"], "x-y", "FirstOf", "FirstOf")
    out_rc_minus_raster.save(f"Height.tif")
    print("Done")

def main():
    #Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    #Execute Prep
    print("Executing Height Prep")
    # Mosaic()
    FillDTM()
    FillDSM()
    Height()
    print("Finished")

if __name__ == "__main__":
    main()