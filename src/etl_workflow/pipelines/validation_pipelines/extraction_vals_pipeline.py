import pandas as pd
from great_expectations.expectations.expectation import ExpectationConfiguration
from great_expectations.core.batch import Batch
from typing import List
from prefect import task,flow
from lib.validations import create_data_batch,create_categorical_expectations,create_set_expectations,validate_expectations


## load the transformed dataframe:
@task
def get_transformed_df(path:str="data/transformed_df.csv")->pd.DataFrame:
    """
    Docstring for get_transformed_df
    
    :param path: path for the transformed dataframe file format
    :type path: str
    :return: dataframe
    :rtype: DataFrame
    """
    df=pd.read_csv("data/transformed_df.csv")

    return df

## create the data batch:
@task
def get_data_batch(df:pd.DataFrame)->Batch:
    """
    Docstring for get_data_batch
    
    :param df: dataframe that will be used for data validation process
    :type df: pd.DataFrame
    :return: batch
    :rtype: Batch
    """
    batch=create_data_batch(df=df)
    
    return batch

## create the target expectations:
@task
def create_expectations():
    cat_exp=create_categorical_expectations(cat_values=[1,0],column_name="Target")
    ##create the age expectations:
    age_exp=create_set_expectations(min_value=41,max_value=80,column_name="age")
    
     ## create the  lcavol expectations:
    cavol_exp=create_set_expectations(min_value=-2,max_value=3.9,column_name="lcavol")
    
     ##lweight expectations:
    weight_exp=create_set_expectations(min_value=2.3,max_value=4.8,column_name="lweight")
    ## gleason expectations:
    gleason_exp=create_set_expectations(min_value=3,max_value=9,column_name="gleason")
    
    ## pgg45 expectations:
    pg_exp=create_set_expectations(min_value=0,max_value=100,column_name="pgg45")
    
    ## create the expectations list:
    exp_list:List[ExpectationConfiguration]=[cat_exp,age_exp,cavol_exp,weight_exp,gleason_exp,pg_exp]

    ## create the corresponding labels:
    exp_labels:List[str]=["target_exp","age","lcavol","lweight","gleason","pgg45"]

    return exp_list,exp_labels
    
def validate_data_exps(batch:Batch,expectations:List[ExpectationConfiguration],exp_labels:List[str])->pd.DataFrame:
    """
    Docstring for validate_data_exps
    
    :param expectations: Description
    :type expectations: List[ExpectationConfiguration]
    :param exp_labels: Description
    :type exp_labels: List[str]
    :return: Description
    :rtype: DataFrame
    """
    results_df=validate_expectations(batch=batch,expectations=expectations,labels=exp_labels)

@flow
def data_validation_pipeline():

    df=get_transformed_df()

    batch=get_data_batch(df=df)

    expectations,exp_labels=create_expectations()

    results_df=validate_data_exps(batch=batch,exp_labels=exp_labels,expectations=expectations)
    
    ## save the results:
    results_df.to_csv("data_quality_checks/data_validation_results.csv",index=False)

if __name__=="__main__":
    data_validation_pipeline()
