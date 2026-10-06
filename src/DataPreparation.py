# Contains the code for the data preparation step
# Each function will address an issue with the dataset

import pandas as pd

def remove_irrelevant_attr(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.drop(columns = ['label', 'tcprtt'])
    return new_df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df
    return new_df

def handle_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df
    return new_df

def convert_data_types():
    pass

def scale_and_standardise():
    pass

def select_attribute():
    pass

def data_instances():
    pass

def correct_class_imbalance():
    pass

def feature_engineering():
    pass
