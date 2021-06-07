import arcpy
from arcpy import env


def tabular_intersection():
    # Set local variables
    in_zone_features = "Garden_Plots.shp"
    zone_fields = "FID"
    in_class_features = "Classified_Garden.shp"
    out_table = "IntersectionTable.dbf"
    class_fields = "gridcode"

    # Execute
    print("Executing Tabular Intersection...")
    arcpy.TabulateIntersection_analysis(in_zone_features, zone_fields, in_class_features, out_table, class_fields)
    print("Done")


def pivot_table():
    # Set local variables
    in_table = "IntersectionTable.dbf"
    fields = "FID_"
    pivot_field = "gridcode"
    value_field = "PERCENTAGE"
    out_table = "PivotTable.dbf"

    # Execute
    print("Executing Pivot table")
    arcpy.PivotTable_management(in_table, fields, pivot_field, value_field, out_table)
    print("Done")


def add_join():
    # First remove unnecessary fields from Garden_Plots
    # Set local variables
    in_table = "Garden_Plots.shp"
    drop_field = ["ogc_fid", "gml_id", "namespace", "begingeldig", "eindgeldig", "tijdstipre", "eindregist",
                  "historievo", "historiest", "akrgemeent", "akrgemee_1", "kadgemeent", "sectie", "perceeln_1",
                  "deltax", "detlay"]

    # Execute
    deleted_fields = arcpy.DeleteField_management(in_table, drop_field)
    arcpy.CopyFeatures_management(deleted_fields, "GardenEssentials.shp")

    # Create the join
    # Set local variables
    in_layer_or_view = "GardenEssentials.shp"
    in_field = "FID"
    join_table = "PivotTable.dbf"
    join_field = "FID_"

    # Execute
    join_table = arcpy.AddJoin_management(in_layer_or_view, in_field, join_table, join_field)
    arcpy.CopyFeatures_management(join_table, "GardenPercent.shp")

    # Create new fields and pervious, impervious and other
    # Set local variables
    # Set local variables
    in_table = "GardenPercent.shp"
    field_name1 = "Pervious"  # first field to be added
    field_name2 = "Impervious"
    field_name3 = "Other"
    field_type = "DOUBLE"

    # Execute
    arcpy.AddField_management(in_table, field_name1, field_type)
    arcpy.AddField_management(in_table, field_name2, field_type)
    arcpy.AddField_management(in_table, field_name3, field_type)

    # Add values to new fields
    # Set local variables
    in_table = "GardenPercent.shp"
    field_1 = "Pervious"
    field_2 = "Impervious"
    field_3 = "Other"
    expression_1 = "!PivotTab_4! + !PivotTab_5! + !PivotTab_6! + !PivotTab_9!"
    expression_2 = "!PivotTab_2! + !PivotTab_3!"
    expression_3 = "!PivotTab_7! + !PivotTab_8!"
    expression_type = "PYTHON3"

    # Execute CalculateField
    arcpy.CalculateField_management(in_table, field_1, expression_1, expression_type)
    arcpy.CalculateField_management(in_table, field_2, expression_2, expression_type)
    arcpy.CalculateField_management(in_table, field_3, expression_3, expression_type)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Calculating classes per zone")
    tabular_intersection()
    print("Merging classes with same value per zone")
    pivot_table()
    print("Join pivot table with garden plot shapefile")
    add_join()
    print("Done")


if __name__ == "__main__":
    main()
