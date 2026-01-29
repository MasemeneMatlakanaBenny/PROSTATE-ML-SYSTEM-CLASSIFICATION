import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from prefect import task,flow
from typing import Union
from lib.configs import X_train_y_train

@task
def get_train_df(path:str="data/train_df")->pd.DataFrame:
    """
    """
    
    train_df=pd.read_csv("data/train_df")
    return train_df
