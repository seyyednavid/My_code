# classification_decision_tree

# Read the data using pandas dataframe
import pandas as pd
# We can convert categorical features such as Sex, BP and Cholesterol  to numerical values
from sklearn import preprocessing
# We will be using train/test split on our decision tree
from sklearn.model_selection import train_test_split
# Modeling(DT classifier)
from sklearn.tree import DecisionTreeClassifier
# Evaluation(accuracy)
from sklearn import metrics
# What operating system/platform the code is running on
from sys import platform
from typing import Tuple


def read_file(file_path: str) -> pd.DataFrame:
    """Reads in a CSV file and returns a pandas dataframe representation"""
    data = pd.read_csv(file_path, encoding="cp1252")
    # Remove the rows including NAN value
    my_data = data.dropna()
    return my_data


class Data(object):
    """Data contains training and test data sets for use in a DT classifier"""

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.dataset = dataset

    def process_data(self, test_size: float, random_state: int, max_depth: int) -> None:
        """
        Process data will validate the input values, will determine the input and output data and will
        split the datasets into training and testing sets
        """
        length: int = len(self.dataset.columns)

        if random_state < 0:
            raise ValueError( "random_state must be between 0 and 2**32 - 1 and must be int")

        if test_size >= 1 or test_size <= 0:
            raise ValueError("test_size should be either positive and float in the (0, 1) range")

        if max_depth <= 0:
            raise ValueError("max_depth must be positive and greater than zero. ")
        elif max_depth > length - 1:
            raise ValueError("max_depth should not be grater than the number of independent values ")

        # The prepared inputData and outputData for using in split_dat function
        self.inputData, self.outputData = self.determine_inputData_outputData(length)
        # 4 outputs of split_data function due to use in train_decision_tree and test_decision_tree functions  
        self.X_trainset, self.X_testset, self.Y_trainset, self.Y_testset = self.split_data(test_size, random_state)
        
           
    def determine_inputData_outputData(self, length: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Function for determining independent variables(inputs) and dependent variable(output)
        """

        # Define independent variables (input or X ) in the form of dataframe (it can be several columns)
        inputData = self.dataset.iloc[:, 0 : length - 1]
        # Define dependent variable (output or Y) in the form of datframe (it can be one column)
        outputData = self.dataset.iloc[:, length - 1 : length]
        # Send input columns to categorise_data function
        update_inputData = self.categorise_data(inputData)
        return update_inputData, outputData
    
 
    def categorise_data(self, input_data: pd.DataFrame) -> pd.DataFrame():
        """
        Transforms a columns categorical features in inputData such as Sex, BP, ...
        to numerical values (from sklearn import preprocessing)
        """
        for i in input_data.columns:

            if i == "Sex":
                le_sex = preprocessing.LabelEncoder()
                le_sex.fit(["F", "M"])
                input_data.iloc[:, 1] = le_sex.transform(input_data.iloc[:, 1])

            if i == "BP":
                le_BP = preprocessing.LabelEncoder()
                le_BP.fit(["LOW", "NORMAL", "HIGH"])
                input_data.iloc[:, 2] = le_BP.transform(input_data.iloc[:, 2])

            if i == "Cholesterol":
                le_Cholesterol = preprocessing.LabelEncoder()
                le_Cholesterol.fit(["LOW", "NORMAL", "HIGH"])
                input_data.iloc[:, 3] = le_Cholesterol.transform(
                    input_data.iloc[:, 3]
                )
        return input_data
    

    def split_data(self, TestSize: float, RandomState: int  ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Populates training and test data sets by splitting the original input data
        """
        # Determine ( X_trainset, Y_trainset) for training  and (X_testset, Y_testset) for testing
        (X_trainset, X_testset, Y_trainset, Y_testset,) = train_test_split(
            self.inputData,
            self.outputData,
            test_size=TestSize,
            random_state=RandomState,
        )
        return X_trainset, X_testset, Y_trainset, Y_testset
    

def train_decision_tree(data: Data, maxDepth) -> DecisionTreeClassifier:
    """Returns a trained Decision Tree Classifier"""
    # Do train based on X_train and Y_train in order to build our model(training stage)
    drugTree = DecisionTreeClassifier(criterion="entropy", max_depth=maxDepth)
    drugTree.fit(data.X_trainset, data.Y_trainset)
    return drugTree
    

def test_decision_tree(data: Data, dt: DecisionTreeClassifier) -> float:
    """Test the Decision Tree against a dataset and evaulate the accuracy"""
    # Predict outputs based on inputs(X_testset) after learning
    predTree = dt.predict(data.X_testset)
    # Comparison of real output (Y_testset) and guessed output(predTree)
    accuracy = metrics.accuracy_score(data.Y_testset, predTree)
    accuracy = round(accuracy, 3)
    return accuracy


def main() -> None:

    file_path = ""
    if platform == "linux" or platform == "linux2":
        file_Path = ""
    elif platform == "darwin":
        file_path = "/Users/danielcrouch/Documents/Konica/Projects/training/python_project/upgrade/drug200.csv"
    elif platform == "win32":
        file_path = "C:/Users/UK021301193/Documents/drug200.csv"

    # Give path to read_file function and get dataset
    dataset = read_file(file_path)

    # Create object c
    c = Data(dataset)
    # Process arguments + determine inputData and outputData + get X,Y_trainset and X,Y_testset for using in train_decision_tree function 
    c.process_data(0.3, 4, 4)

    # Create decisionTree and do train based on X_train and Y_train in order to build our model
    dt = train_decision_tree(c, 4)
    # Predict outputs and gain the accuracy 
    accuracy = test_decision_tree(c, dt)
    print("accuracy: " , accuracy)


if __name__ == "__main__":
    main()