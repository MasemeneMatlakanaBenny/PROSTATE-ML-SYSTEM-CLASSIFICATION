import pandas as pd
from sklearn.model_selection import train_test_split


df=pd.read_csv("data/transformed_df.csv")

## get the label:
drop_columns=["datetime","userID"]

df=df.drop(drop_columns,axis=1)

##train and test sets
train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)


## save both train and test sets to a csv format
train_df.to_csv("data/train_df.csv",index=False)
test_df.to_csv("data/test_df.csv",index=False)

