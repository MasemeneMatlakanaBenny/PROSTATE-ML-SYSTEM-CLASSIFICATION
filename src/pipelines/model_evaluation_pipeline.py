import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from prefect import task,flow
from typing import Union
from lib.configs import X_train_y_train



##load the model first:
def load_model(path:str)->Union[LogisticRegression,DecisionTreeClassifier]:

    model=joblib.load(path)
    return model
