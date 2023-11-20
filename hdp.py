# -*- coding: utf-8 -*-
"""HDP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DvvJ3lwEeREQifYp3g1EZJLApznilwQ_
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn import linear_model, tree, ensemble

dataframe=pd.read_csv("/content/drive/MyDrive/heart_disease_data.csv")
dataframe.head(10)

dataframe.info()

dataframe.isna().sum()

plt.figure(figsize=(15,10))
sns.heatmap(dataframe.corr(),linewidth=.01,annot=True,cmap="winter")
plt.show()
plt.savefig('correlationfigure')

dataframe.hist(figsize=(12,12))
plt.savefig('featuresplot')

dataframe['target'].value_counts()

X = dataframe.drop(columns='target', axis=1)
Y = dataframe['target']

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=2)

from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

tree_model = DecisionTreeClassifier(max_depth=5,criterion='entropy')
cv_scores = cross_val_score(tree_model, X, Y, cv=10, scoring='accuracy')
m=tree_model.fit(X, Y)
prediction=m.predict(X_test)
cm= confusion_matrix(Y_test,prediction)
sns.heatmap(cm, annot=True,cmap='winter',linewidths=0.3, linecolor='black',annot_kws={"size": 20})
print(classification_report(Y_test, prediction))

TP=cm[0][0]
TN=cm[1][1]
FN=cm[1][0]
FP=cm[0][1]
print(round(accuracy_score(prediction,Y_test)*100,2))
print('Testing Accuracy for Decision Tree:',(TP+TN)/(TP+TN+FN+FP))
print('Testing Sensitivity for Decision Tree:',(TP/(TP+FN)))
print('Testing Specificity for Decision Tree:',(TN/(TN+FP)))
print('Testing Precision for Decision Tree:',(TP/(TP+FP)))

input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)
input_as_numpy = numpy.asarray(input_data)
input_reshaped = input_as_numpy.reshape(1, -1)
pre1 = tree_model.predict(input_reshaped)

if pre1[0] == 1:
    print("The patient seems to have heart disease:(")
else:
    print("The patient seems to be Normal:)")

input=(63,3,2,145,233,1,1,150,3,2.3,1,1,1)
input_as_numpy=np.asarray(input)
input_reshaped=input_as_numpy.reshape(1,-1)
pre1=tree_model.predict(input_reshaped)
if(pre1==1):
  print("The patient seems to be have heart disease:(")
else:
  print("The patient seems to be Normal:)")