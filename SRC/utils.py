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
    







 

