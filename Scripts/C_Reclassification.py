import arcpy
from arcpy import env


def reclassify_class_image():
    in_raster = "Classified.tif"
    reclass_field = "Classvalue"
    remap = "0 15 10;15 25 20;25 35 40;35 45 30;45 55 40"
    out_raster = "RC_Class.tif"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/reclassify.htm
    print("Executing Reclassification")
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")
    print("Done")


def reclassify_ground_truth():
    # Set local variables for reclassification
    in_table = "TrainingSamples.shp"
    field = "Classvalue"
    expression = "Reclass(!Classvalue!)"
    expression_type = "PYTHON3"
    code_block = """
# Reclassify values to another value
# More calculator examples at esriurl.com/CalculatorExamples
def Reclass(Classvalue):
    if Classvalue == 10:
        return 10
    elif Classvalue == 20:
        return 20
    elif Classvalue == 30:
        return 30
    elif Classvalue == 40:
        return 40
    elif Classvalue == 50:
        return 30 """

    # Execute CalculateField
    print("Reclassifying water to other")
    arcpy.CalculateField_management(in_table, field, expression, expression_type, code_block)

    # Set local variables to dissolve and merge water and other
    in_features = "TrainingSamplesOriginal.shp"
    out_feature_class = "RC_Training.shp"
    dissolve_field = "Classvalue"

    # Execute dissolve
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/dissolve.htm
    print("Dissolving water and other")
    arcpy.Dissolve_management(in_features, out_feature_class, dissolve_field)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Reclassifying Classified Image")
    reclassify_class_image()
    print("Reclassifying Training Samples")
    reclassify_ground_truth()
    print("Done")


if __name__ == "__main__":
    main()
