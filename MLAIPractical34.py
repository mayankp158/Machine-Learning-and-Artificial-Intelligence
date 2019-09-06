import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

#seprate array into input and output component
X = array[:,0:8] #(0 to 7)
Y = array[:,8] #9th column
scaler = StandardScaler()

#first method
standardX = scaler.fit_transform(X)

#summarize transformed data
set_printoptions(precision=2)
print( standardX[:20,:])


