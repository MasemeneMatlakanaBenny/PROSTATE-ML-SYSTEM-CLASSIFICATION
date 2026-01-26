import pandas as pd
from great_expectations.expectations.expectation import ExpectationConfiguration
from great_expectations.core.batch import Batch
from typing import List
from lib.validations import create_data_batch,create_categorical_expectations,create_set_expectations,validate_expectations


## load the transformed dataframe:
df=pd.read_csv("data/transformed_df.csv")

## create the data batch:
batch=create_data_batch(df=df)

## create the target expectations:
cat_exp=create_categorical_expectations(cat_values=[1,0],column_name="Target")

##create the age expectations:
age_exp=create_set_expectations(min_value=41,max_value=80,column_name="age")

## create the min lcavol expectations:
cavol_exp=create_set_expectations(min_value=-2,max_value=3.9,column_name="lcavol")

## lweight expectations:
weight_exp=create_set_expectations(min_value=2.3,max_value=4.8,column_name="lweight")

## gleason expectations:
gleason_exp=create_set_expectations(min_value=3,max_value=9,column_name="gleason")

## pgg45 expectations:
pg_exp=create_set_expectations(min_value=0,max_value=100,column_name="pgg45")

## create the expectations list:
exp_list:List[ExpectationConfiguration]=[cat_exp,age_exp,cavol_exp,weight_exp,gleason_exp,pg_exp]

## create the corresponding labels:
exp_labels:List[str]=["target_exp","age","lcavol","lweight","gleason","pgg45"]

## get the results df:
results_df=validate_expectations(batch=batch,expectations=exp_list,labells=exp_labels)

## save the results:
results_df.to_csv("data_quality_checks/data_validation_results.csv",index=False)
