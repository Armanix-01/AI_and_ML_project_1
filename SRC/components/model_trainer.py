## here we are train different models  and check their metrics and
#  then choose best models.
import pandas as pd
import numpy as np
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from SRC.exception import CustomException
from SRC.logger import logging

from SRC.utils import save_object, evaluate_models
from dataclasses import dataclass
import sys
import os
from catboost import CatBoostRegressor


##Dataclass way of making class is optimal when we just need class
# to store some data and not some methods or specifically complex
# methods.
@dataclass
class ModelTrainerConfig:

    trained_model_file_path:str = os.path.join("artifacts", "model.pkl")



class ModelTrainer:
    def __init__(self):
        
        self.model_trainer_config = ModelTrainerConfig()
        ## Here model_trainer_config is variable and variable can 
        # contain objects


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("splittraining and test input data")
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1] )
            

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            """Here in models values here you are giving the
            instance of the class not defining the class so 
            when you train these instances in model_evaluate
            Then since value by referencing happens therefore
            these values of models inturn gets trained"""

            model_report:dict = evaluate_models(
                x_train, y_train, x_test, y_test, models
            )

            ##To get the best model from dictionary
            best_model_score = max(sorted(model_report.values()))
            ##To get the best model_name from dictionary
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")


            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )
            predicted  = best_model.predict(x_test)
            r2 = r2_score(predicted, y_test)

            return r2


        except Exception as e:
            raise CustomException(e, sys)
