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

