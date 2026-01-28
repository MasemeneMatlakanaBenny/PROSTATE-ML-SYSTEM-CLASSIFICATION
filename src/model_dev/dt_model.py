import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from lib.configs import X_train_y_train

train_df=pd.read_csv("data/train_df")

## get the X_train and y_train sets:
X_train,y_train=X_train_y_train(train_df=train_df)

## train the model:
model=DecisionTreeClassifier(criterion="entropy",min_samples_split=4)
## fit the model:
model.fit(X_train,y_train)

## save the model:
joblib.dump(model,"models/dt_model.pkl")
