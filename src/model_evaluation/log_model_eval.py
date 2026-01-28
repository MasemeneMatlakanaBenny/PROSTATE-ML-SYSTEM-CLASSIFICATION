import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from lib.configs import model_metrics,X_train_y_train

##load the model first:
model:LogisticRegression=joblib.load("models/log_model.pkl")

## load X_test and y_test:
test_df=pd.read_csv("data/test_df.csv")
X_test,y_test=X_train_y_train(test_df)

## compute the model metrics:
metrics=model_metrics(y_true=y_test,X_test=X_test,model=model)

## save the model metrics in a pickle file:
joblib.dump(metrics,"metrics/log_model_metrics.pkl")

