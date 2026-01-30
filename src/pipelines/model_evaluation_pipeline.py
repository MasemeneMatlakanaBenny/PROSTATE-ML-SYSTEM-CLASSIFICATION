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

@task
def get_test_sets(path:str)->pd.DataFrame:
      """
    Docstring for get_test_sets
    
    :param path: Description
    :type path: str
    :return: Description
    :rtype: DataFrame
    """
     
    df=pd.read_csv(path)

    X_test,y_test=X_train_y_train(train_df=df)

    return X_test,y_test

## compute the model metrics:
@task
def get_model_metrics(X_test,y_test,model:Union[LogisticRegression,DecisionTreeClassifier]):
    """
    Docstring for get_model_metrics
    
    :param X_test: Description
    :param y_test: Description
    :param model: Description
    :type model: Union[LogisticRegression, DecisionTreeClassifier]
    """
    metrics=model_metrics(y_true=y_test,X_test=X_test,model=model)

    return metrics

@flow
def model_evaluation_workflow():
    """
    """
    log_model=load_model(path="models/log_model.pkl")
    dt_model=load_model(path="models/dt_model.pkl")
    X_test,y_test=X_train_y_train("data/test_df.csv")
     
    log_model_metrics=get_model_metrics(X_test=X_test,y_test=y_test,model=log_model)
    dt_model_metrics=get_model_metrics(X_test=X_test,y_test=y_test,model=dt_model)

