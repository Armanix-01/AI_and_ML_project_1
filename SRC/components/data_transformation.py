##We will transform the data here like cat to num
import sys
from dataclasses import dataclass
import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
"""sklearn.impute is a module in scikit-learn that provides tools
 to handle missing values in your dataset.

Think of it as the “missing data fixer” in scikit-learn.

✅ What it does
It fills in (imputes) missing values in numerical or categorical 
columns.

🔧 Main classes inside sklearn.impute
1️⃣ SimpleImputer

Fills missing values using a simple rule:

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")       # for numbers
imputer = SimpleImputer(strategy="most_frequent")  # for categories


Strategies:
"mean" → replace with average value
"median" → replace with median
"most_frequent" → replace with mode
"constant" → replace with a custom value

2️⃣ KNNImputer

Fills missing values using nearest neighbors.

from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)


It looks at rows similar to the incomplete row and fills missing values based on their data.

3️⃣ IterativeImputer

Advanced imputer → uses regression-style estimation:

from sklearn.impute import IterativeImputer


It predicts missing values based on other columns.

4️⃣ MissingIndicator

Creates an extra column for whether the value was missing or not."""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


from SRC.logger import logging 
from SRC.exception import CustomException
from SRC.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join("artifacts", "presprocessor.pkl")




class DataTransformation:
    def __init__(self):
        self.DataTransformationConfig = DataTransformationConfig()


    def get_data_transformer_obj(self):
        try:
            numerical_features = ["writing_score", "reading_score"]
            categorical_features = ["gender", "race_ethnicity",
                                    "parental_level_of_education",
                                    "test_preparation_course"]
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("One_hot_encoder", OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean= False))
                ]
            )
            logging.info("numerical columns pre_processing completed")
            logging.info("categorical columns pre_processing completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )
            return preprocessor
        
        except Exception as e:


            raise CustomException(e, sys)
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("read train and test completed")
            logging.info("now obtaining preprocessing object from get_data_transfer_obj fn")

            preprocessing_obj = self.get_data_transformer_obj()
            target_column_name = "math_score"
            numerical_columns_name = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr  = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logging.info("saved preprocessing obj")

            save_object(
                file_path = self.DataTransformationConfig.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )


            """In Python's NumPy library, np.c_[] is a powerful 
            utility for translating slice objects and 
            array-likes into concatenation along the second axis
            (columns). It is a shorthand way to stack items
             horizontally
             
             import numpy as np
             a = np.array([1, 2, 3])
             b = np.array([4, 5, 6])
             result = np.c_[a, b]
             
             Output: array([[1, 4],
                            [2, 5],
                            [3, 6]])

             
             """
            return(
                train_arr,
                test_arr,
                self.DataTransformationConfig.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)

