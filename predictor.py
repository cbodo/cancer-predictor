import pandas as pd
import numpy as np
import random
from sklearn import linear_model, metrics, model_selection
from columnnames import COLUMN_NAMES

# import csv
url = "./Cancer_Data.csv"
data = pd.read_csv(url)
df = pd.DataFrame(data,columns=COLUMN_NAMES)

# convert target column from categorical to numerical
df['diagnosis'].replace(['B', 'M'], [0, 1], inplace=True)

# create logistic regression model with max iterations set to 10000
log_model = linear_model.LogisticRegression(max_iter=10000)

# define the independent (X) and dependent (y) sets 
X = df.drop(columns=['diagnosis'])
y = df[['diagnosis']].copy()

# create the training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.333, random_state=41)

# train the model
log_model.fit(X_train.values,np.ravel(y_train))

# generate predictions set
y_pred_log = log_model.predict(X_test.values)

 # Accuracy Analysis

# Calculate Accuracy (where accuracy = correct predictions / total predictions)
accuracy_score = f"Accuracy Score: {metrics.accuracy_score(y_test, y_pred_log)}"

# Calculate Mean Squared Error
# Measure of the difference between predicted and actual values.
mse = f"Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred_log)}"

# Cross-validation. 
y_array = np.ravel(y.values)
k_folds = model_selection.KFold(n_splits = 5, shuffle=True)
scores = model_selection.cross_val_score(log_model, X, y_array)
scores_mean = f"Cross Validation Average Score: {scores.mean()}"

# defines function to generate a random number for an attribute in a range from the min value in the dataset to the max value in the dataset for that attribute
def generate_rand(attribute):
    min_val = df[str(attribute)].describe()['mean']-2*df[str(attribute)].describe()['std']
    max_val = df[str(attribute)].describe()['mean']+2*df[str(attribute)].describe()['std']
    return random.uniform(min_val, max_val)