import arcpy
from arcpy import env


def raster_to_polygon():
    # Set local variables
    in_raster = "Final_Classes.tif"
    out_polygon_features = "Final_Class_Polygon.shp"
    field = "VALUE"

    # Execute
    arcpy.RasterToPolygon_conversion(in_raster, out_polygon_features, "NO_SIMPLIFY", field)


def extract_gardens():
    # Set local variables
    in_features = "Final_Class_Polygon.shp"
    clip_features = "Garden_Plots.shp"
    out_feature_class = "Classified_Garden.shp"

    # Execute Clip
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Creating Polygon")
    raster_to_polygon()
    print("Extracting Gardens")
    extract_gardens()
    print("Done")


if __name__ == "__main__":
    main()
