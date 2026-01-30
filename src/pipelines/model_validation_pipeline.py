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
    
    :param path: path of the model
    :type path: str
    :return:expecting a Logistic Regression or Decisioon Tree Trained Models since only these two have been trained. It should
    be noted that one can add the type annotation depending on the type of the models that have been trained
    :rtype: LogisticRegression | DecisionTreeClassifier
    """

    model=joblib.load(path)

    return model

@task
def get_model_metrics(path:str)->Dict:
    """
    Docstring for get_model_metrics
    
    :param path: Description
    :type path: str
    :return: Description
    :rtype: Dict
    """
    metrics=joblib.load(path)

    return metrics

@task
def metrics_dataframe(metrics:Dict)->pd.DataFrame:
    """
    Docstring for metrics_dataframe
    
    :param metrics: Description
    :type metrics: Dict
    :return: Description
    :rtype: DataFrame
    """
    metrics_df=pd.DataFrame([metrics])

    return metrics_df
