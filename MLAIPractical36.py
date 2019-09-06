import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

#seprate array into input and output component
X = array[:,0:8] #(0 to 7)
Y = array[:,8] #9th column
binarizer = Binarizer(threshold=5)

#first method
binaryX = binarizer.fit_transform(X)

#summarize transformed data
set_printoptions(precision=2)
print( binaryX[:20,:])

