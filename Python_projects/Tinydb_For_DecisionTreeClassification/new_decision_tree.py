#Classification_decision_tree
import pandas as pd                                     # Read the data using pandas dataframe
from sklearn.model_selection import train_test_split    # We will be using train/test split on our decision tree
from sklearn import metrics                             # Evaluation
from sklearn.tree import DecisionTreeClassifier         # Modeling
from sklearn import preprocessing                       # We can convert categorical features such as Sex, BP and Cholesterol  to numerical values
from typing import Tuple                                # Show static type
from tinydb import TinyDB                               # Create tinydb



class Decision_Tree(object):
    
    def __init__(self, file: str, test_size: float, random_state: int, max_depth: int) -> None:
                
        self.my_data =  pd.read_csv(file, encoding = 'cp1252')                 # Read data by pandas from csv file
        self.length: int = len(self.my_data.columns)                           # Number of columns
        self.X = self.my_data.iloc[:, 0: self.length -1]                       # Define independent variables
        self.Y = self.my_data.iloc[:, self.length -1: self.length]             # Define dependent variable
        self.test_size = test_size                                             # It determins how many percent for test and the rest for train 
        self.random_state = random_state                                       # The random_state ensures that we obtain the same splits
        self.max_depth = max_depth                                             # The depth of decision tree
        self.answer: float = 0                                                 # Answer
        self.db = TinyDB('db.monitor')                                         # Create tinydb that is called db.monitor                                                    # 
        self.convert_cat_to_num()                                              # Convert  categorical features to numerical values
        self.traintest_split(self.X, self.Y)                                   # Send prepared input , output for traintest_split
        
    
        
    
    def convert_cat_to_num(self) -> None:
        """
        This function updates inputData(self.X) categorical features such as Sex, BP, ... 
        to numerical values (from sklearn import preprocessing)  
        """
        
        for i in self.X.columns:
             
             if i == 'Sex':                              
               le_sex = preprocessing.LabelEncoder() 
               le_sex.fit(['F', 'M'])
               self.X.iloc[:, 1] = le_sex.transform(self.X.iloc[:, 1])
              
             if i == 'BP':
               le_BP = preprocessing.LabelEncoder()
               le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
               self.X.iloc[:, 2] = le_BP.transform(self.X.iloc[:, 2])
            
             if i == 'Cholesterol':
              le_Cholesterol = preprocessing.LabelEncoder()
              le_Cholesterol.fit(['LOW', 'NORMAL', 'HIGH'])
              self.X.iloc[:, 3] = le_Cholesterol.transform(self.X.iloc[:, 3])
             
    
    
              
    def traintest_split(self, X: pd.DataFrame, Y:pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        '''
         This function is for using train/test split on our decision tree
         (from sklearn.model_selection import train_test_split)
        '''
        
        if isinstance(self.random_state, float):                               # Check input(random_state)
            raise TypeError ("please enter int value")
            
        elif  isinstance(self.random_state, str):
            raise TypeError ("please enter int value")
        else:
            pass
        
        if self.test_size >= 1 or self.test_size <= 0:                         # Check input(test_size)
            raise ValueError("test_size should be either positive and float in the (0, 1) range")
        else:
            pass
        
        X_trainset, X_testset, Y_trainset, Y_testset = train_test_split(X, Y, test_size = self.test_size, random_state = self.random_state)
        # Determine X and Y for train and test
        
        return self.model(X_trainset, X_testset, Y_trainset, Y_testset)
    
    
        
    
    def model(self , X_trainset: pd.DataFrame, X_testset: pd.DataFrame, Y_trainset: pd.DataFrame, Y_testset: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
         Function for building a model (from sklearn.tree import DecisionTreeClassifier) 
        '''
        
        if self.max_depth <= 0:                                                # Check input(max_depth)
            raise ValueError("max_depth must be positive and greater than zero.")
        if isinstance(self.max_depth, float):
            raise TypeError ("please enter int value")
        if self.max_depth > self.length - 1:
            raise ValueError("max_depth should not be grater than the number of independent values ")
            
        drugTree = DecisionTreeClassifier(criterion = "entropy", max_depth = self.max_depth)
        # Use decision tree with desired max_depth
        
        drugTree.fit(X_trainset, Y_trainset)     
        # Do train based on X_train and Y_train in order to build our model(training stage)
                  
        predTree = drugTree.predict(X_testset)
        # Predict outputs based on inputs(X_testset) after learning(based on model) 
        
        return self.evalution(Y_testset, predTree )
    
    
    
    
    def evalution(self, Y_test: pd.DataFrame, Y_predictTree: pd.DataFrame ) -> float:
        '''
        # Function for Evaluation(from sklearn import metrics)    
        '''
        
        self.answer = metrics.accuracy_score(Y_test, Y_predictTree )
        # Comparison of real output (Y_test) and guessed output(Y_preictTree)
        
        return (self.answer)
    
    
        
    
    def result(self) -> None:
        '''
         Save our results in db  
        '''
        length_db = len(self.db)
        on = False
        i: int = 1
        
        while i < length_db + 1 :
            item = self.db.get(doc_id = i)
            if  item['test_size'] == self.test_size and item['random_state'] == self.random_state and item['max_depth'] == self.max_depth:
            # If inputs is repetitive  , retrieving result from db
               result = item['result']
               on = True
               print(result)
               break
           
            else:
                  i = i + 1
                  
        if on == True:
           pass
       
        else:
        # new input gives new output so it should  be saved to db
          self.db.insert({'test_size': self.test_size, 'random_state': self.random_state, 'max_depth': self.max_depth, 'result': round(self.answer, 3)})
          
        

c = Decision_Tree("C:/Users/UK021301193/Documents/drug200.csv", 0.39, 2, 2) 
c.result()
  

       

