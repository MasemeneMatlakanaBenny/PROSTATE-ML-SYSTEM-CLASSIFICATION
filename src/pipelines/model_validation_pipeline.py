import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from great_expectations.core.batch import Batch
from great_expectations.expectations.expectation import ExpectationConfiguration
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
    
    :param path: path of the model metrics
    :type path: str
    :return: metrics of the model
    :rtype: Dict
    """
    metrics=joblib.load(path)

    return metrics

@task
def metrics_dataframe(metrics:Dict)->pd.DataFrame:
    """
    Docstring for metrics_dataframe
    
    :param metrics: metrics in a dictionary format
    :type metrics: Dict
    :return: metrics in a dataframe after converting the metrics dictionary into a usable dataframe format
    :rtype: DataFrame
    """
    metrics_df=pd.DataFrame([metrics])

    return metrics_df

@task
def model_batch(metrics_df)->Batch:
    """
    Docstring for model_batch
    
    :param metrics_df: model evaluation metrics in a dataframe
    :return: batch that will be used to validate the model based on the metrics
    :rtype: Batch
    """

    batch=create_model_batch(df=metrics_df)

    return batch

