import pandas as pd
import great_expectations as gx
from great_expectations.expectations.expectation import ExpectationConfiguration
from great_expectations.core.batch import Batch
from typing import List,Union


## create the batch:
def create_data_batch(df:pd.DataFrame)->Batch:
    """
    Docstring for create_data_batch
    
    :param df: dataframe that will be used for validation process
    :type df: pd.DataFrame
    :return: batch that will validate data expectations and quality checks
    :rtype: Batch
    """

    ## create the context first
    context=gx.get_context()

    ## create the data source:
    data_source=context.data_sources.add_pandas("pandas_source")

    ## create the data asset:
    data_asset=data_source.add_dataframe_asset("data_asset")

    ## create the batch definition:
    batch_definition=data_asset.add_batch_definition_whole_dataframe("batch_definition")

    ## create the batch:
    batch=batch_definition.get_batch(batch_parameters={"df":df})

    return batch

## start by creating data expectations:
def create_categorical_expectations(cat_values:List[str],
                                    column_name:str)->ExpectationConfiguration:
    """
    Docstring for create_categorical_expectations
    
    :param cat_values: list of categorical values in the column
    :type cat_values: List[str]
    :param column_name: name of the column to be validated
    :type column_name: str
    :return: data expectation that will be validated
    :rtype: ExpectationConfiguration
    """
    
    expectation=gx.expectations.ExpectColumnDistinctValuesToEqualSet(
        column=column_name,value_set=cat_values
    )

    return expectation

def create_set_expectations(min_value:Union[int,float],
                            max_value:Union[int,float],
                            column_name:str)->ExpectationConfiguration:
    """
    Docstring for create_set_expectations
    
    :param min_value: min value expected of the column
    :type min_value: Union[int, float]
    :param max_value: max value expected of the column
    :type max_value: Union[int, float]
    :param column_name: name of the column
    :type column_name: str
    :return: data expectation that will be validated
    :rtype: ExpectationConfiguration
    """

    expectation=gx.expectations.ExpectColumnValuesToBeBetween(
        min_value=min_value,max_value=max_value,column=column_name
    )

    return expectation

def validate_expectations(batch:Batch,expectations:List[ExpectationConfiguration],labels:List[str])->pd.DataFrame:
    """
    Docstring for validate_expectations
    :param batch:batch that will be used to validate the data expectations
    :type batch:Batch
    :param expectations: data expectations that will be validated
    :type expectations: List[ExpectationConfiguration]
    :param labels: corresponding expectation labels
    :type labels: List[str]
    :return: dataframe of the validated results
    :rtype: DataFrame
    """
    results=[]
    for exp in expectations:
        validation=batch.validate(exp)
        result=validation[0]

        results.append(result)

    df=pd.DataFrame({"expectation":labels,"results":results})

    return df

def meta_validations(batch:Batch)->str:
    """
    Docstring for meta_validations
    
    :param batch: batch that will be used to validate the data expectations or quality tests to ensure correctness and accuracy
    :type batch: Batch
    :return: success if all the data quality checks have been passed
    :rtype: str
    """
    expectation=gx.expectations.ExpectColumnDistinctValuesToEqualSet(
        column="results",value_set=["success"]
    )

    results=batch.validate(expectation)[0]

    return results


