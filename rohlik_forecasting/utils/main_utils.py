import os
import sys
import numpy as np
from pandas import DataFrame
import dill
import yaml
from rohlik_forecasting.logger import logging
from rohlik_forecasting.exception import RohlikForecastException

def initial_analysis(dataset):
    #shape of the dataset
    
    print("\n The shape of the dataset:{}".format(dataset.shape))
    print("\n Number of columns in the dataset:{}".format(dataset.shape[1]))
    print("\n Number of rows in the dataset:{}".format(dataset.shape[0]))
    print("\n Data types in the dataset :\n \n{}".format(dataset.dtypes))
    print("*"*45)
    
       
    # Numerical and Categorical feautres in the dataset
    
    numeric_features = dataset.select_dtypes(include = [np.number])
    categoric_features = dataset.select_dtypes(exclude = [np.number])
    print(" Number of Numerical Features : {}".format(numeric_features.shape[1]))
    print("\n Number of Categorical Features : {}".format(categoric_features.shape[1]))
    print("Numerical Features: \n", numeric_features.columns)
    print("Categorical Features: \n", categoric_features.columns)
    print("*"*40)
    
    # Missing values
    print(" Number of missing values :\n \n{}".format(dataset.isna().sum()))
    print("*"*40)
    
    # Checking the duplicates
    print("\n**The dataset has {} duplicate rows.**".format(dataset.duplicated().sum()))
    
    return initial_analysis
############################################################################################################
def read_yaml(file_path:str)->dict:
    """
    Read yaml file
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error(e)
        raise RohlikForecastException(e,sys) from e
############################################################################################################   
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise RohlikForecastException(e, sys) from e
############################################################################################################
def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise RohlikForecastException(e, sys) from e
    
############################################################################################################

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise RohlikForecastException(e, sys) from e
    
############################################################################################################


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise RohlikForecastException(e, sys) from e

############################################################################################################


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise RohlikForecastException(e, sys) from e

############################################################################################################

def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise RohlikForecastException(e, sys) from e