# test decision_tree_classification

import unittest
from numpy import float64    
import pandas as pd
from unittest.mock import patch, Mock, MagicMock
from sklearn.tree import DecisionTreeClassifier
from new_decision_tree import Data  
from new_decision_tree import read_file
from new_decision_tree import train_decision_tree
from new_decision_tree import test_decision_tree
import numpy as np


class TestDecisionTree(unittest.TestCase):

    test_size1 = 0.3        
    random_state1 = 4
    max_depth1 = 4
    
    test_size2 = 0.6      
    random_state2 = 4
    max_depth2 = 3
    

    def setUp(self):

        self.dataset = pd.DataFrame({"Age": [23, 47, 47], "Sex": ['F', 'M', 'M'], "BP": ['HIGH', 'LOW', 'LOW'], 
                         "Cholesterol": ['HIGH', 'HIGH', 'HIGH'], "Na_to_K": [25.355, 13.093, 10.114], "Drug": ['drugY', 'drugC', 'drugC']})
        

    def tearDown(self):
        pass

##################################################
    
    def test_pandas_read_csv(self):
        """ Check the Read_file function(get csv file and give pd.DataFram)"""
        with patch("pandas.read_csv") as read_csv_mock:
            read_csv_mock.return_value = self.dataset
            my_data = read_file("file/path/file.csv")
            read_csv_mock.assert_called_with("file/path/file.csv", encoding="cp1252")
            self.assertTrue(my_data.equals(self.dataset))
        
    
    def test_Read_file_removing_NaN_value(self): 
        """ Check that remove the rows including NAN value"""
        with patch("pandas.read_csv") as read_csv_mock:
            read_csv_mock.return_value = pd.DataFrame({"Age": [23, 47, 47], "Sex": ['F', np.nan, 'M'], "BP": ['HIGH', 'LOW', 'LOW'], 
                         "Cholesterol": ['HIGH', 'HIGH', 'HIGH'], "Na_to_K": [25.355, 13.093, 10.114], "Drug": ['drugY', 'drugC', 'drugC']})
            data = read_file("file/path/file.csv")
            my_data = data.dropna()
            read_csv_mock.assert_called_with("file/path/file.csv", encoding="cp1252")
            my_data.equals(pd.DataFrame({"Age": [23, 47], "Sex": ['F', 'M'], "BP": ['HIGH', 'LOW'], 
                         "Cholesterol": ['HIGH', 'HIGH'], "Na_to_K": [25.355, 10.114], "Drug": ['drugY', 'drugC']}))
             
##################################################

    def test_Data_init(self):
        """ Test input in __init__"""
        c = Data(self.dataset)
        self.assertTrue(c.dataset.equals(self.dataset))

#################################################

    def test_process_data_invalid_random_state(self):
        """ Test the value of random_state (random_state < 0)"""
        random_state3 = -1
        with self.assertRaises(ValueError) as ex:
            c = Data(self.dataset)
            c.process_data(self.test_size1, random_state3, self.max_depth1)
            self.assertEqual(str(ex.exception), "random_state must be between 0 and 2**32 - 1 and must be int")

    
    def test_process_data_invalid_test_size(self):
        """ Test the values of test size """
        test_size3 = 1.5
        test_size4 = 0 
        with self.assertRaises(ValueError) as ex:
            c = Data(self.dataset)
            # test size >= 1
            c.process_data(test_size3, self.random_state1, self.max_depth1)
            self.assertEqual(str(ex.exception),"test_size should be either positive and float in the (0, 1) range")
            
        with self.assertRaises(ValueError) as exp:
            c = Data(self.dataset)
            # test size <= 0
            c.process_data(test_size4, self.random_state1, self.max_depth1)
            self.assertEqual(str(exp.exception), "test_size should be either positive and float in the (0, 1) range")


    def test_process_data_invalid_max_depth(self):
        """ Test the values of max_depth"""
        max_depth3 = 0
        max_depth4 = 6
        with self.assertRaises(ValueError) as ex:
            c = Data(self.dataset)
            # max_depth <= 0
            c.process_data(self.test_size1, self.random_state1, max_depth3)
            self.assertEqual(str(ex.exception), "max_depth must be positive and greater than zero")
            
        with self.assertRaises(ValueError) as exp:
            c = Data(self.dataset)
            # max_depth > length - 1 => (5)
            c.process_data(self.test_size1, self.random_state1, max_depth4)
            self.assertEqual(str(exp.exception), "max_depth should not be grater than the number of independent values")

##################################################
   
    def test_determine_inputData_outputData(self):
        "Check to divide columns correctly for inputData and outputData"
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        self.assertEqual(len(c.inputData.columns), 5)
        self.assertEqual(len(c.outputData.columns), 1)

##################################################

    def test_categorise_data_Sex_type(self):
        "Check Sex feature turn into numerical type"
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        c.categorise_data(self.dataset)    
        x = str(self.dataset.Sex.dtype)
        if x == "int64":
               Sex_dtype = {x}
        elif x == "int32":
               Sex_dtype = {x}
        elif x == "int16":
             Sex_dtype = {x}
        else:   
            pass
        myset = {"int64", "int32", "int16"}
        self.assertTrue(set(Sex_dtype).issubset(set(myset)))
        
        
    def test_categorise_data_BP_type(self):
        "Check BP feature turn into numerical type"
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        c.categorise_data(self.dataset)    
        x = str(self.dataset.BP.dtype)
        if x == "int64":
               BP_dtype = {x}
        elif x == "int32":
               BP_dtype = {x}
        elif x == "int16":
             BP_dtype = {x}
        else:
            pass
        myset = {"int64", "int32", "int16"}
        self.assertTrue(set(BP_dtype).issubset(set(myset)))

    
    def test_categorise_data_Cholesterol_type(self):
        "Check Cholesterol feature turn into numerical type"
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        c.categorise_data(self.dataset)    
        x = str(self.dataset.BP.dtype)
        if x == "int64":
               Cholesterol_dtype = {x}
        elif x == "int32":
               Cholesterol_dtype = {x}
        elif x == "int16":
             Cholesterol_dtype = {x}
        else:
            pass
        myset = {"int64", "int32", "int16"}
        self.assertTrue(set(Cholesterol_dtype).issubset(set(myset)))
        
        
    def test_categorise_data_value(self):
        """ Turn categorical features into numerical values """
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        c.inputData.equals(pd.DataFrame({"Age": [23, 47, 47], "Sex": [0, 1, 1], "BP": [0, 1, 1], "Cholesterol": [0, 0, 0], "Na_to_K": [25.355, 13.093, 10.114]}))
        
###############################################################
 
    def test_split_data_X_trainset(self):
         """ Check the number of rows for X_trainset depend on test_size"""
         c = Data(self.dataset)
         # Test_size(0.3)-> 0.3 for test and 0.7 for train
         c.process_data(self.test_size1, self.random_state1, self.max_depth1)
         self.assertEqual(len(c.X_trainset), 2)
         
         # Test_size(0.6)-> 0.6 for test and 0.4 for train
         c.process_data(self.test_size2, self.random_state2, self.max_depth2)
         self.assertEqual(len(c.X_trainset), 1)
         
         
    def test_split_data_Y_trainset(self): 
         """ Check the number of rows for Y_trainset depend on test_size"""
         c = Data(self.dataset)
         # test_size(0.3)-> 0.3 for test and 0.7 for train
         c.process_data(self.test_size1, self.random_state1, self.max_depth1)
         self.assertEqual(len(c.X_trainset), 2)
         
         # test_size(0.6)-> 0.6 for test and 0.4 for train
         c.process_data(self.test_size2, self.random_state2, self.max_depth2)
         self.assertEqual(len(c.X_trainset), 1)

   
    def test_split_data_X_testset(self): 
         """ Check the number of rows for X_testset depend on test_size"""
         c = Data(self.dataset)
         # test_size(0.3)-> 0.3 for test and 0.7 for train
         c.process_data(self.test_size1, self.random_state1, self.max_depth1)
         self.assertEqual(len(c.X_testset), 1)
         
         # test_size(0.6)-> 0.6 for test and 0.4 for train
         c.process_data(self.test_size2, self.random_state2, self.max_depth2)
         self.assertEqual(len(c.X_testset), 2)

    
    def test_split_data_Y_testset(self):
         """ Check the number of rows for X_testset depend on test_size"""
         c = Data(self.dataset)
         # test_size(0.3)-> 0.3 for test and 0.7 for train
         c.process_data(self.test_size1, self.random_state1, self.max_depth1)
         self.assertEqual(len(c.Y_testset), 1)
         
         # test_size(0.6)-> 0.6 for test and 0.4 for train
         c.process_data(self.test_size2, self.random_state2, self.max_depth2)
         self.assertEqual(len(c.Y_testset), 2)
    
###################################################################
     
    def test_train_decision_tree(self):
        "Check train_decision_tree's output"
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        

        with patch("new_decision_tree.DecisionTreeClassifier") as mock_decision_tree:
            a = train_decision_tree(c, self.max_depth1)

            mock_decision_tree.assert_called_with(
                criterion="entropy", max_depth=self.max_depth1
            )
            a.fit.assert_called_with(c.X_trainset, c.Y_trainset)

       
###################################################################
    
    def test_test_decision_tree_accuracy_by_one_predict(self):
        """" Check the accuracy""" 
        c = Data(self.dataset)
        c.process_data(self.test_size1, self.random_state1, self.max_depth1)
        dt = train_decision_tree(c, self.max_depth1)       
        dt = MagicMock() 
        # With one Y_testset(because of test_size = 0.3) and false predict
        dt.predict.return_value = ['drugY']
        accuracy = test_decision_tree(c, dt)
        dt.predict.assert_called_with(c.X_testset)
        self.assertEqual(accuracy, 0.0)
        
        # With one Y_testset(because of test_size = 0.3) and true predict
        dt.predict.return_value = ['drugC']
        accuracy = test_decision_tree(c, dt)
        dt.predict.assert_called_with(c.X_testset)
        self.assertEqual(accuracy, 1.0)
        
        
    
    def test_test_decision_tree_accuracy_by_two_predict(self):
        """" Check the accuracy """
        c = Data(self.dataset)
        c.process_data(self.test_size2, self.random_state2, self.max_depth2)
        dt = train_decision_tree(c, self.max_depth2)       
        dt = MagicMock() 
        # With two Y_testset(because of test_size = 0.6), one false predict and one true predict
        dt.predict.return_value = ['drugC', 'drugC']
        accuracy = test_decision_tree(c, dt)
        dt.predict.assert_called_with(c.X_testset)
        self.assertEqual(accuracy, 0.5)
        
         
if __name__ == '__main__':
    unittest.main()          
        
