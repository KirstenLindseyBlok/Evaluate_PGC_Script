import arcpy
from arcpy import env


def reclassify_class_image():
    in_raster = "Classified.tif"
    reclass_field = "Classvalue"
    remap = "0 15 10;15 25 20;25 35 30"
    out_raster = "RC_Class.tif"

    # Execute
    print("Executing Reclassification")
    arcpy.Reclassify_3d(in_raster, reclass_field, remap, out_raster, "NODATA")
    print("Done")


def reclassify_ground_truth():
    # Set local variables for reclassification
    in_table = "GroundTruthSamples.shp"
    field = "Classvalue"
    expression = "Reclass(!Classvalue!)"
    expression_type = "PYTHON3"
    code_block = """
# Reclassify values to another value
# More calculator examples at esriurl.com/CalculatorExamples
def Reclass(Classvalue):
    if Classvalue == 10:
        return 20
    elif Classvalue == 20:
        return 10
    elif Classvalue == 30:
        return 30
    elif Classvalue == 40:
        return 20
    elif Classvalue == 50:
        return 30 """

    # Execute CalculateField
    print("Reclassifying Ground Truth")
    arcpy.CalculateField_management(in_table, field, expression, expression_type, code_block)

    # Set local variables to dissolve and merge unwanted classes
    in_features = "GroundTruthSamples.shp"
    out_feature_class = "RC_GroundTruth.shp"
    dissolve_field = "Classvalue"

    # Execute dissolve
    print("Dissolving unwanted classes")
    arcpy.Dissolve_management(in_features, out_feature_class, dissolve_field)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    env.overwriteOutput = True
    print("Reclassifying Classified Image")
    reclassify_class_image()
    print("Reclassifying Training Samples")
    reclassify_ground_truth()
    print("Done")


if __name__ == "__main__":
    main()
