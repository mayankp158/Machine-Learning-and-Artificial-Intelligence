import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

import warnings
warnings.filterwarnings("ignore")
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)


#1). Spot checking for Logistic Regression

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
results = cross_val_score(model, X,Y, cv=kfold)
print("Validation Score for Logistic Regression:", results.mean())

#2). Spot checking for Linear Discriminant Analysis(LDA)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X,Y, cv=kfold)
print("Validation Score for LDA:", results.mean())
results.mean()

#3). Spot checking for kNN
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
results = cross_val_score(model, X,Y, cv=kfold)
print("Validation Score for kNN:", results.mean())

#4). Spot checking for Gausian Naive Bayes

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
results = cross_val_score(model,X,Y, cv= kfold)
print("Validation Score for GaussianNB:", results.mean())

# 5). Spot checking for CART

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
results = cross_val_score(model,X,Y, cv= kfold)
print("Validation Score for CART Decision Tree:", results.mean())

# 5). Spot checking for SVM

from sklearn.svm import SVC
model = SVC()
results = cross_val_score(model,X,Y, cv= kfold)
print("Validation Score for SVM:", results.mean())








