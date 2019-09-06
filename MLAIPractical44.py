import pandas as pd
from sklearn.model_selection import ShuffleSplit
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

test_datasize = 0.33
no_of_repetitions = 10
shufflesplit = ShuffleSplit(n_splits=no_of_repetitions,
                            test_size=test_datasize)

model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=shufflesplit)
print(result)
print()
print("Accuracy= %.3f" % ( result.mean()*100.0))
print()
print("Standard Deviation= %.3f" % ( result.std()*100.0))
