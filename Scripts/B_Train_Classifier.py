import arcpy
from arcpy import env
from arcpy.sa import *

def Train_Classifier():
    # Set local variables
    in_Raster = "Mosaic_ir.tif"
    train_features = "C:/Users/kirstenb/PycharmProjects/PGC_Project/Input_Data_Prep/Data/TrainingSamplesOriginal.shp"
    out_definition = "ClassDefinition.ecd"
    in_additional_raster = "segmented_ir.tif"
    maxNumSamples = "0"
    attributes = "COLOR;COUNT;COMPACTNESS;RECTANGULARITY"
    dimension_value_field = "Classvalue"

    # Execute
    # https://pro.arcgis.com/en/pro-app/latest/tool-reference/image-analyst/train-support-vector-machine-classifier.htm
    TrainSupportVectorMachineClassifier(in_Raster, train_features, out_definition, in_additional_raster, maxNumSamples, attributes, dimension_value_field)

def main():
    # Set geoprocessing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/Evaluate_PGC_Script/Data"
    env.overwriteOutput = True
    print("Executing Classifier Training")
    Train_Classifier()
    print("Classifier Training Finished")

if __name__ == "__main__":
    main()