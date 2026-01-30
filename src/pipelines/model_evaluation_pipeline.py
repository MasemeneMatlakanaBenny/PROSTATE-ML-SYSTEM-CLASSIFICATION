import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from prefect import task,flow
from typing import Union
from lib.configs import X_train_y_train



##load the model first:
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

def get_test_sets(path:str)->pd.DataFrame:
    df=pd.read_csv(path)

    X_test,y_test=X_train_y_train(train_df=df)

    return X_test,y_test
