import pandas as pd
from numpy import set_printoptions #roundoff after decimals
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

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
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X,Y)
result = fit.transform(X)

print("Num Features: ", fit.n_features_ )
print("Selected Features: ", fit.support_)
print("Feature Ranking: ", fit.ranking_)
print("\n\n\n", result[:20, :])


