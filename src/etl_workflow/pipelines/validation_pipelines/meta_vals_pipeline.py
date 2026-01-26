import pandas as pd
from great_expectations.core.batch import Batch
from typing import List
from lib.validations import create_data_batch,meta_validations
from prefect import task,flow

## load df:
@task
def get_validation_results_df(path:str="data_quality_checks/data_validation_results.csv")->pd.DataFrame:
    """
    Docstring for get_validation_results_df
    
    :param path: Description
    :type path: str
    :return: Description
    :rtype: DataFrame
    """
    df=pd.read_csv(path)
    
    return df

## create the batch:
@task
def run_meta_validation(df:pd.DataFrame)->str:
    """
    Docstring for run_meta_validation
    
    :param df: Description
    :type df: pd.DataFrame
    :return: Description
    :rtype: str
    """
    
    batch=create_data_batch(df=df)
    
    ## create meta vals:
    meta_results=meta_validations(batch=batch)
    
    print(meta_results)

@flow
def meta_data_validation_pipeline():

    vals_df=get_validation_results_df()

    run_meta_validation()

if __name__=="__main__":
    meta_data_validation_pipeline()

    
