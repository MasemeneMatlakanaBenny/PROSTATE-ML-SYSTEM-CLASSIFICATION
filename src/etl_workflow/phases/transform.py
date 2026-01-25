import numpy as np
import pandas as pd
from datetime import datetime

##load the extracted data:
df=pd.read_csv("data/extracted_df.csv")

## transform it by adding the unique userID and datetime:
df['userID']=np.arange(1,len(df)+1)

df['datetime']=datetime.now()


## save the transformed dataframe to data folder:
df.to_csv("data/transformed_df",index=False)
