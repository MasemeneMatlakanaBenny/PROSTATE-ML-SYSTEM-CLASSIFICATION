import pandas as pd


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

