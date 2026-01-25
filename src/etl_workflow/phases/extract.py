import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()

## load the credentials of the database:
user=os.getenv("USER")
table_name=os.getenv("TABLE_NAME")
schema_name=os.getenv("SCHEMA")
password=os.getenv("PASSWORD")
host = "127.0.0.1"
port = "3306"
user = "root"

db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema_name}"

engine=create_engine(db_url)

query="SELECT * FROM {table_name}"

df=pd.read_sql_query(engine=engine,query=query)

df.to_csv("data/extracted_df.csv")
