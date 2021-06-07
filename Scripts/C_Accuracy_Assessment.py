from arcpy import env
from arcpy.sa import *


def ground_truth():
    # Set local variables
    in_class_data = "RC_Training.shp"
    out_points = "Ground_Truth.shp"
    target_field = "GROUND_TRUTH"
    num_random_points = "1000"
    sampling = "STRATIFIED_RANDOM"

    # Execute
    CreateAccuracyAssessmentPoints(in_class_data, out_points, target_field, num_random_points, sampling)


def accuracy_assessment():
    # Set local variables
    in_class_data = "RC_Class.tif"
    in_points = "Ground_Truth.shp"
    out_points = "AccuracyAssessment"
    target_field = "CLASSIFIED"

    # Execute
    UpdateAccuracyAssessmentPoints(in_class_data, in_points, out_points, target_field)


def confusion_matrix():
    # Set local variables
    in_accuracy_assessment_points = "AccuracyAssessment.shp"
    out_confusion_matrix = "ConfusionMatrix.dbf"

    # Execute
    ComputeConfusionMatrix(in_accuracy_assessment_points, out_confusion_matrix)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Creating Ground Truth Points")
    ground_truth()
    print("Complete Accuracy Assessment")
    accuracy_assessment()
    print("Create Confusion Matrix")
    confusion_matrix()
    print("Done")


if __name__ == "__main__":
    main()
