import arcpy
from arcpy import env

def Raster_to_Polygon():
    #Set local variables
    in_raster = "Final_Classes.tif"
    out_polygon_features = "Final_Class_Polygon.shp"
    field = "VALUE"

    #Execute
    #https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/raster-to-polygon.htm
    arcpy.RasterToPolygon_conversion(in_raster, out_polygon_features, "NO_SIMPLIFY", field)

def Extract_Gardens():
    #Set local variables
    in_features = "Final_Class_Polygon.shp"
    clip_features = "Garden_Plots.shp"
    out_feature_class = "Classified_Garden.shp"

    #Execute Clip
    #https: // pro.arcgis.com / en / pro - app / latest / tool - reference / analysis / clip.htm
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    print("Creating Polygon")
    Raster_to_Polygon()
    print("Extracting Gardens")
    Extract_Gardens()
    print("Done")

if __name__ == "__main__":
    main()