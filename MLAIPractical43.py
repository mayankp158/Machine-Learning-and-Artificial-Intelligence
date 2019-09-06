import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings("ignore")


filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values

X = array[:,0:8]
Y = array[:,8]

loocv = LeaveOneOut()
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=loocv)

print("results :" , result)
print()
print()
print("result size :" ,result.size)
print()
print("Sum of Positive Results: %i" % (result.sum()))
print()
print("Accuracy= %.2f%%" % (
    result.sum() * 100 / result.size))

#comparing y and y'