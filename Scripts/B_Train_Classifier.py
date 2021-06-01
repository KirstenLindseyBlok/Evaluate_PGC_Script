import arcpy
from arcpy import env
from arcpy.sa import *

def Train_Classifier():
    # Set local variables
    in_Raster = "segmented_ir.tif"
    train_features = "TrainingSamplesOriginal.shp"
    out_definition = "ClassDefinition.ecd"
    in_additional_raster = ""
    maxNumSamples = "0"
    attributes = "COLOR;COUNT;COMPACTNESS;RECTANGULARITY"
    dimension_value_field = "Classvalue"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/train-support-vector-machine-classifier.htm
    TrainSupportVectorMachineClassifier(in_Raster, train_features, out_definition, in_additional_raster, maxNumSamples, attributes, dimension_value_field)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/Kirsten/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing Classifier Training")
    Train_Classifier()
    print("Classifier Training Finished")

if __name__ == "__main__":
    main()