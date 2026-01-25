import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from prefect import task,flow


load_dotenv()

@task
def get_credentials():
    """
    Docstring for get_credentials
    """
    ## load the credentials of the database:
    user=os.getenv("USER")
    table_name=os.getenv("TABLE_NAME")
    schema_name=os.getenv("SCHEMA")
    password=os.getenv("PASSWORD")
    host = "127.0.0.1"
    port = "3306"
    user = "root"
    
    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema_name}"

    return db_url

@task
def create_engine_task(db_url):
    """
    Docstring for create_engine_task
    
    :param db_url: Description
    """
    engine=create_engine(db_url)
    query="SELECT * FROM {table_name}"

    return engine,query

@task
def get_extracted_data(engine,query)->pd.DataFrame:
    """
    Docstring for get_extracted_data
    
    :param engine: Description
    :param query: Description
    :return: Description
    :rtype: DataFrame
    """

    df=pd.read_sql_query(engine=engine,query=query)

    return df

@flow
def extraction_pipeline():
    db_url=get_credentials()
    engine,query=create_engine_task()

    df=get_extracted_data(engine=engine,query=query)

    df.to_csv("data/extracted_df.csv",index=False)


if __name__=="__main__":
    extraction_pipeline()
