import pandas as pd
import os
import hopsworks
from dotenv import load_dotenv


## load .env file:
load_dotenv()

## get the project name from .env file:
project_name=os.getenv("PROJECT_NAME")
api_key=os.getenv("API_KEY")

## get the transformed data:
df=pd.read_csv("transformed_df.csv")

## login hopsworks
project=hopsworks.login(
    project=project_name,
    api_key_value=api_key
)

## get the feature store:
feature_store=project.get_feature_store()

## get the feature view:
feature_group=feature_store.get_or_create_group(
    name="Prostate Feature Group",
    description="View for the prostate ML project",
    event_time="datetime",
    primary_key="userID"
)

feature_group.insert(df,write_options={"wait_for_job":False})



## Create the feature pipeline:
feature_view=feature_store.get_or_create_feature_view(
name="Prostate Feature View",
version=1,
labels=[],
logging_enabled=True)

