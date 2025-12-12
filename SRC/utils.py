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

## to make code more cleaner we could have made
def save_object(file_path:str,
                obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as  file_obj:
        dill.dump(obj,file_obj)

    