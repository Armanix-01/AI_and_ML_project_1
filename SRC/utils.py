##This contains any fnctionality that will be used in the 
# entire application.
#Lets say i want to read a data from the database so i can 
# create my mongo client like mongoDB client over here 
# OR I want to save my model in the cloud, i can write my 
# code here and i can try to call it inside the components 
# itself.


"""A utils.py file contains reusable helper functions
that can be used across the entire project."""
import os
import pandas as pd
import numpy as np
import sys
from SRC.exception import CustomException
from SRC.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import pickle

## to make code more cleaner we could have made
def save_object(file_path:str,
                obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as  file_obj:
        dill.dump(obj,file_obj)

    

def evaluate_models(x_train, y_train, x_test, y_test, models, params):
    
    try:
       report= {}
       for model_name, model in models.items():
            


            param = params.get(model_name,{})
            ##This params.get(key, default_value) basically tells
            # “Give me the value for this key; if it doesn’t exist, 
            #  return the default.”
            gs = GridSearchCV(
                estimator= model,
                param_grid= param,
                cv=3,
                n_jobs= -1
            )
            gs.fit(x_train, y_train)
            best_model = gs.best_estimator_
        
            models[model_name] = best_model
            
            """Best Parameters: gs.best_params_ gives you a
            dictionary of the specific hyperparameter values
            (e.g., {'C': 10, 'kernel': 'rbf'}) that yielded
                the highest cross-validation score.
            
            Best Estimator: gs.best_estimator_ gives you a full,
                instantiated, and fitted model object that was 
                created using those exact best_params_"""
            
            y_train_pred = best_model.predict(x_train)
            y_test_pred = best_model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            """When using sklearn.metrics.r2_score(a, b), the first
            positional argument a must be the true values (y_true)
            , and the second argument b must be the predicted 
            values (y_pred)"""
            
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score
       return report
    
    except Exception as e:
       
       raise CustomException(e, sys)


##ANOTHER METHOD
'''def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
        
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
'''

"""model.set_params(**gs.best_params_)
here gs.best_params_ returns a dict of hypertuned parameters 
and using ** is know as **kwargs(keyword arguments unpacking)
here What it means
A dictionary is unpacked into named arguments
Keys → parameter names
Values → parameter values """
    
def load_obj(file_path):
    with open(file_path, 'rb') as obj:
        return pickle.load(obj)


##Serialization
'''Serialization in Python is the process of converting complex
data structures or objects into a format that can be easily 
stored, transmitted over a network, and later reconstructed.
This process is also known as pickling when using Python's 
built-in pickle module. 
The reverse process of converting the serialized format back
into a usable Python object is called deserialization 
(or unpickling). '''


## Uses of Serialization
'''Serialization is used in various scenarios:
1. Data Persistence: Saving the state of an object or application 
to a file for later use (e.g., saving game progress or user
 preferences).
2. Data Transmission: Sending data between different systems 
or processes over a network (e.g., web APIs use JSON for data
 interchange).
3. Caching: Storing complex, time-consuming computed data in a 
fast-access format to improve performance.
'''
 
##Pickle load and dump
'''The terms load and dump are fundamental function names used i
n Python's standard libraries, most notably json and pickle, 
to manage the process of serialization and deserialization.

dump is used to write (serialize) Python objects to a file.
load is used to read (deserialize) data from a file into a Python
object.
In simpler terms, you dump data into a storage medium (like a 
file), and you load data out of that storage medium back into
memory.'''

##Dill
'''In Python, dill is a third-party library that acts as an 
extension of the built-in pickle module, providing more robust
serialization capabilities. It is designed to serialize a wider
range of Python objects that pickle cannot handle by default. 

Why use dill?
The standard pickle module can serialize most basic Python 
objects (like lists, dictionaries, integers, and custom class 
instances), but it often fails on more complex or "exotic" types,
such as: 
1. Functions defined in an interactive session (like a Jupyter
 notebook)
2. lambda functions
3. Nested functions and closures
4. Entire modules or interpreter sessions
5. File handles and their contents 

dill addresses these limitations by serializing the object's 
code and dependencies, not just its state, making it a powerful
tool for scenarios like distributed computing, where complex   
functions need to be sent across different processes. '''