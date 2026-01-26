import pandas as pd
from great_expectations.core.batch import Batch
from typing import List
from lib.validations import create_data_batch,meta_validations

## load df:
df=pd.read_csv("data_quality_checks/data_validation_results.csv")

## create the batch:
batch=create_data_batch(df=df)

## create meta vals:
meta_results=meta_validations(batch=batch)

print(meta_results)
