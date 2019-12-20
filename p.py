import numpy as np
import pandas as pd
import urllib

import sklearn
from sklearn.naive_bayes import BernoulliNB

from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import accuracy_score




# making data frame from csv file
data = pd.read_csv("datasets.csv")
xx = data.to_numpy()
# creating a dataframe from list
df = pd.DataFrame(data)
X = df.iloc[0:100]

print(type(xx))
print(xx)