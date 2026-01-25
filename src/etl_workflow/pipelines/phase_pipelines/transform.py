import numpy as np
import pandas as pd
from datetime import datetime
from prefect import task,flow

##load the extracted data:
@task
def get_extracted_df(path:str="data/extracted_df.csv")->pd.DataFrame:
    """
    Docstring for get_extracted_df
    
    :param path: path of extracted data 
    :type path: str
    :return: extracted data in a dataframe format
    :rtype: DataFrame
    """
    df:pd.DataFrame=pd.read_csv(path)

    return df

@task
def transform_data(df:pd.DataFrame)->pd.DataFrame:
    """
    Docstring for transform_data
    
    :param df: the raw/extracted data in a dataframe format
    :type df: pd.DataFrame
    :return: transformed dataframe  
    :rtype: DataFrame
    """
    ## transform it by adding the unique userID and datetime:
    df['userID']=np.arange(1,len(df)+1)
    df['datetime']=datetime.now()

@flow
def transformation_pipeline():
    df=get_extracted_df()

    transformed_df=transformed_df(df=df)
    ## save the transformed dataframe to data folder:
    transformed_df.to_csv("data/transformed_df",index=False)

if __name__=="__main__":
    transformation_pipeline()
