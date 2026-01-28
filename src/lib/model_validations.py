import pandas as pd
import great_expectations as gx
from great_expectations.expectations.expectation import ExpectationConfiguration
from great_expectations.core.batch import Batch
from typing import List,Union


## create the batch:
def create_model_batch(df:pd.DataFrame)->Batch:
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

def create_metric_expectation(min_value:Union[int,float],max_value:Union[int,float],metric_name:str)->ExpectationConfiguration:
    """
    Docstring for create_metric_expectation
    
    :param min_value: minimum value of the metric
    :type min_value: Union[int, float]
    :param max_value: maximum value of the metric
    :type max_value: Union[int, float]
    :param metric_name: name of the metric
    :type metric_name: str
    :return: expectation
    :rtype: ExpectationConfiguration
    """

    expectation=gx.expectations.ExpectColumnValuesToBeBetween(
        min_value=min_value,max_value=max_value,column=metric_name
    )

    return expectation

def validate_metric_expectations(batch:Batch,expectations:List[ExpectationConfiguration],labels:List[str])->pd.DataFrame:
    """
    Docstring for validate_metric_expectations
    :param batch:batch that will be used to validate the metric expectations
    :type batch:Batch
    :param expectations: metric expectations that will be validated
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

def meta_metric_validations(batch:Batch)->str:
    """
    Docstring for meta_metric_validations
    
    :param batch: Description
    :type batch: Batch
    :return: Description
    :rtype: str
    """
    expectation=gx.expectations.ExpectColumnDistinctValuesToEqualSet(
        column="results",value_set=["success"]
    )

    results=batch.validate(expectation)[0]

    return results



