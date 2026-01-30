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

@task
def model_metrics_expectation():
    
    """
    """

    accuracy_exp=create_metric_expectation(min_value=0.8,max_value=0.9,metric_name="accuracy")
    kappa_exp=create_metric_expectation(min_value=0.8,max_value=0.9,metric_name="kappa_score")
    mat_exp=create_metric_expectation(min_value=0.8,max_value=0.9,metric_name="mat_corr")
    gilbert_exp=create_metric_expectation(min_value=0.8,max_value=0.95,metric_name="gilbert_score")

    model_exp:List[ExpectationConfiguration]=[accuracy_exp,kappa_exp,mat_exp,gilbert_exp]
    exp_labels:List[str]=["accuracy","kappa","matthews_corr","gilbert_skill_score"]

    return model_exp,exp_labels

