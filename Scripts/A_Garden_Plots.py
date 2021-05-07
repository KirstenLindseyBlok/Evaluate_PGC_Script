import arcpy
from arcpy import env

def SelectByAttribute():
    #Set local Variables
    in_features = "Tuinen.shp"
    out_layer = "TuinenLayer.shp"

    #Make a layer from the feature class
    arcpy.MakeFeatureLayer_management(in_features, out_layer)

    #Set local Variables
    in_layer_or_view = "TuinenLayer.shp"
    selection_type = "NEW_SELECTION"
    where_clause = "BGT_FYSIEK = 'erf'"

    #Select all polygons that are have a bgt_fysiek value of 'erf'
    gardens = arcpy.SelectLayerByAttribute_management(in_layer_or_view, selection_type, where_clause)

    #Write the selected features to a new feature class
    arcpy.CopyFeatures_management(gardens, 'Gardens.shp')
    print("Extracting Private Gardens Completed")

def Clip():
    #Set local variables
    in_features = "Percelen.shp"
    clip_features = "Gardens.shp"
    out_feature_class = "Garden_Plots.shp"

    #Execute Clip
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
    print("Extracting Private Gardens Per Plot Completed")

def main():
    #Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    #Execute Prep
    print("Execute Garden Plot Prep")
    SelectByAttribute()
    Clip()
    print("Garden Plot Prep Finished")

if __name__ == "__main__":
    main()