##Reading the data
'''Data ingestion refers to the process of importing, transferring,
or loading data from various external sources into a system or
storage infrastructure'''

import os 
'''This is the built in standard library that provides a portable
way to interact with underlying operating system. it allows 
devs to perform operations such as managing files, directories, 
environment variables, and executing system commands.'''
import sys
'''What does sys module or library do?
sys module in python allows us to access system specific
parameters, variables, functions that interact directly with 
python runtime variable and interpretor.
                  or
sys module in Python = System-specific utilities.
It gives your Python program access to things related to the 
Python interpreter and the system environment

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
x_train=ct.fit_transform(x_train)'''
from SRC.exception import CustomException
from SRC.logger import logging
from SRC.components.data_transformation import DataTransformation,DataTransformationConfig
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
"""✅ 1. from
This tells Python that you want to import something specific 
from a module.

Think of it like:
“From this package, give me this particular item.”

✅ 2. dataclasses

This is the module (a built-in Python library in Python 3.7+).
It provides a feature called data classes, which makes writing 
classes easier by automatically creating:

__init__()
__repr__()
__eq__()
and other boilerplate methods

You normally use it when a class is mainly for storing data.

✅ 3. import

This keyword means:
“Bring this thing into my code so I can use it.”

✅ 4. dataclass

This is the decorator inside the dataclasses module.
You use it like this:
@dataclass
class Student:
    name: str
    age: int

@dataclass automatically creates:
an initializer → __init__(self, name, age)
a nice string representation → `"Student(name='Aman', age=20')"
equality check methods
etc.

So you don’t need to write all that manually."""

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts', 'train.csv')
    test_data_path: str= os.path.join("artifacts", "test.csv")
    raw_data_path: str= os.path.join("artifacts", "data.csv")

## usually we make a different folder by the name CONFIG but here
# for understanding we are configuring here, these are the paths
#  where we will save the output

class DataIngestion:
    """if you dont have other functions inside the class the 
    use dataclass otherwise use def__init__ method
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        ## If ur data is stored somewhere then we use this code to 
        # call it
        logging.info("Entered the data_ingestion method and component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset")

            ##Lets create all the directories
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path ,header=True, index=False)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index =False, header =True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data =obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
