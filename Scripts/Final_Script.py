import A_Garden_Plots
import A_Height
import A_Imagery
import B_Segmentation
import B_Train_Classifier
import B_Classification
import C_Reclassification
import C_Accuracy_Assessment
import D_Final_Classification
import D_Classification_of_Gardens
import E_Percentage_of_Garden

def DataPrep():
    #Prep Garden Plots
    A_Garden_Plots.main()
    #Prep Height Data
    A_Height.main()
    #Prep Imagery
    A_Imagery.main()

def Classification():
    #Segmentation
    B_Segmentation.main()
    #Train Classifier
    B_Train_Classifier.main()
    #Classification
    B_Classification.main()

def AccuracyAssessment():
    C_Reclassification.main()
    C_Accuracy_Assessment.main()

def Final_Classification():
    D_Final_Classification.main()
    D_Classification_of_Gardens.main()

def Percentage():
    E_Percentage_of_Garden.main()

def main():
    print("Initiating Data Prep")
    DataPrep()
    print("Data Prep Completed")
    print("Innitiating Initial Classification")
    Classification()
    print("Initial Classification Completed")
    print("Innitiating Accuracy Assessment")
    AccuracyAssessment()
    print("Accuracy Assessment Completed")
    print("Innitiating Final Classification")
    Final_Classification()
    print("Final Classification Completed")
    print("Initiating Percentage Calculation")
    Percentage()
    print("Percentage Calculation Completed")
    print("PGC Project Completed")

if __name__ == "__main__":
    main()