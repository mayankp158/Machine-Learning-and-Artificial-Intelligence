import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

#seprate array into input and output component
X = array[:,0:8] #(0 to 7)
Y = array[:,8] #9th column
scaler = MinMaxScaler(feature_range=(1,5))

#first method
rescaledX = scaler.fit_transform(X)

#summarize transformed data
set_printoptions(precision=2)
print( rescaledX[:20,:])