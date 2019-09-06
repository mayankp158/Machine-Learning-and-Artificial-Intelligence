import pandas as pd
from numpy import set_printoptions #roundoff after decimals
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values

#seprate array into input and output component
X = array[:,0:8] #(0 to 7)
Y = array[:,8] #9th column

#feature extraction
test = SelectKBest(score_func=chi2, k=4) #best 4 cloumn
fit = test.fit(X,Y)

#summarize score
set_printoptions(precision=3)
print( fit.scores_)
features = fit.transform(X)


print("\n\n")
print(features[0:20,:])


