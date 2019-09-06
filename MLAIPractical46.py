import pandas as pd
from sklearn.model_selection import KFold
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

model = LogisticRegression()

scoringMethod = 'neg_log_loss'

num_folds = 10

kfold = KFold(n_splits=num_folds)
result = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print("result :" , result)
print()
print("Logloss: = %.3f " % (result.mean()))
print()
print("Standard Deviation: = %.3f" % ( result.std()))

#more logloss close to zero more correct answer

