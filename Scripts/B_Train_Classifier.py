from arcpy import env
from arcpy.sa import *


def train_classifier():
    # Set local variables
    in_raster = "segmented_ir.tif"
    train_features = "TrueTrainingSamples.shp"
    out_definition = "ClassDefinition.ecd"
    in_additional_raster = ""
    max_num_samples = "0"
    attributes = "COLOR;COUNT;COMPACTNESS;RECTANGULARITY"
    dimension_value_field = "Classvalue"

    # Execute
    TrainSupportVectorMachineClassifier(in_raster, train_features, out_definition, in_additional_raster,
                                        max_num_samples, attributes, dimension_value_field)


def main():
    # Set geo-processing environments
    env.workspace = "C:/Users/kirstenb/PycharmProjects/FinalReport/Data"
    env.overwriteOutput = True
    print("Executing Classifier Training")
    train_classifier()
    print("Classifier Training Finished")


if __name__ == "__main__":
    main()
