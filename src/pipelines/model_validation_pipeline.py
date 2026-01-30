import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from prefect import task,flow
from typing import Union,Dict

@task
def load_model(path:str)->Union[LogisticRegression,DecisionTreeClassifier]:
    """
    Docstring for load_model
    
    :param path: Description
    :type path: str
    :return: Description
    :rtype: LogisticRegression | DecisionTreeClassifier
    """

    model=joblib.load(path)

    return model
