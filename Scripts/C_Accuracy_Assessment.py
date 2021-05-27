import arcpy
from arcpy import env
from arcpy.sa import *

def Ground_Truth():
    #Set local variables
    in_class_data = "RC_Training.shp"
    out_points = "Ground_Truth.shp"
    target_field = "GROUND_TRUTH"
    num_random_points = "1000"
    sampling = "STRATIFIED_RANDOM"

    #Execute
    #https: // pro.arcgis.com / en / pro - app / latest / tool - reference / image - analyst / create - accuracy - assessment - points.htm
    CreateAccuracyAssessmentPoints(in_class_data, out_points, target_field, num_random_points, sampling)

def Accuracy_Assessment():
    #Set local variables
    in_class_data = "RC_Class.tif"
    in_points = "Ground_Truth.shp"
    out_points = "AccuracyAssessment"
    target_field = "CLASSIFIED"

    #Execute
    #https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/update-accuracy-assessment-points.htm
    UpdateAccuracyAssessmentPoints(in_class_data, in_points, out_points, target_field)

def Confusion_Matrix():
    #Set local variables
    in_accuracy_assessment_points = "AccuracyAssessment.shp"
    out_confusion_matrix = "ConfusionMatrix.dbf"

    #Execute
    #https: // pro.arcgis.com / en / pro - app / latest / tool - reference / spatial - analyst / compute - confusion - matrix.htm
    ComputeConfusionMatrix(in_accuracy_assessment_points, out_confusion_matrix)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/PGC_Project/Input_Data_Prep/Data"
    env.overwriteOutput = True
    print("Creating Ground Truth Points")
    Ground_Truth()
    print("Complete Accuracy Assessment")
    Accuracy_Assessment()
    print("Create Confusion Matrix")
    Confusion_Matrix()
    print("Done")

if __name__ == "__main__":
    main()