##we will be creating the simple web application which will be
# interacting with these pickle files(any input data we give).
"""Lets say web application will have a form where we will POST
out data that data will be captured in the backend and that data
will need to interact with these pickle files and we get a prediction
"""
import sys
import os
import pandas as pd
import numpy as np
from SRC.exception import CustomException
from SRC.utils import load_obj


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','presprocessor.pkl')
            print("Before Loading")
            model=load_obj(file_path=model_path)
            preprocessor=load_obj(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        

        except Exception as e:
            raise CustomException(e,sys)

##Here we are basically taking 
class CustomData:
    def __init__(self,
                gender:str,
                race_ethnicity:str,
                parental_level_of_education:str,
                lunch:str,
                test_preparation_course:int,
                reading_score:int,
                writing_score:int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course =test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)



        
