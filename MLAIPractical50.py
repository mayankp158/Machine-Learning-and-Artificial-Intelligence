import pandas as pd

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")
filename = 'housing.csv'
hnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX','RM', 'AGE',
          'DIS', 'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values

X = array[:,0:13]
Y = array[:,13]

kfold= KFold(n_splits=10, random_state=7)
model = LinearRegression()

scoringMethod = 'neg_mean_absolute_error' #avg of absolute value

result = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print("MAE: %.3f (%.3f)" % (result.mean(), result.std()))

