import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from typing import List,Union


def X_train_y_train(train_df:pd.DataFrame):
    """
    Docstring for X_train_y_train
    
    :param train_df: Description
    :type train_df: pd.DataFrame
    """
    label="Target"

    X_train=train_df.drop(label,axis=1)
    y_train=train_df[label]

    return X_train,y_train

def gilbert_skill_score(y_true,y_pred):
    from sklearn.metrics import confusion_matrix as conf_mat

    tp,fp,fn,tn=conf_mat(y_true,y_pred).ravel()
    e=tp*(fp+fn)/len(y_true)

    gss=(tp-e)/(tp+fp+fn-e)

    return gss

def model_metrics(y_true,
                  X_test,
                  model:Union[LogisticRegression,DecisionTreeClassifier]):
    from sklearn.metrics import accuracy_score,cohen_kappa_score,matthews_corrcoef
    y_pred=model.predict(X_test)
    acc_score=accuracy_score(y_true,y_pred)
    kappa_score=cohen_kappa_score(y_true,y_pred)
    mat_score=matthews_corrcoef(y_true,y_pred)
    gilbert_score=gilbert_skill_score(y_true,y_pred)

    return {"accuracy":acc_score,"kappa_score":kappa_score,"mat_corr":mat_score,"gilbert_score":gilbert_score}
  

