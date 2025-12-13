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

## to make code more cleaner we could have made
def save_object(file_path:str,
                obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as  file_obj:
        dill.dump(obj,file_obj)

    

def evaluate_models(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for x in range(len(list(models))):
            model = list(models.values())[x]
            model.fit(x_train, y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_model_score = r2_score(y_pred= y_train_pred, y_true= y_train)
            test_model_score = r2_score(y_pred= y_test_pred, y_true= y_test)

            report[list(models.keys())[x]] = test_model_score

        return report
      
    except Exception as e:
        raise CustomException(e, sys)

"""for model_name, model in models.items():
    model.fit(x_train, y_train)
"""##This is the industry standard


