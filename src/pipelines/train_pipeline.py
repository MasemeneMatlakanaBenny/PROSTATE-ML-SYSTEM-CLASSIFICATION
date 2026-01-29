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

@task
def load_X_set_y_set(train_df:pd.DataFrame):
    
    ## get the X_train and y_train sets:
    X_train,y_train=X_train_y_train(train_df=train_df)
    return X_train,y_train

## train the model:
@task
def train_logistic_reg_model(X_train,y_train)->LogisticRegression:
    
    model=LogisticRegression(solver="liblinear")

    ## fit the model:
    model.fit(X_train,y_train)

    return model
