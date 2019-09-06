#also known as extremely randomized tree classifier
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier

import warnings
warnings.filterwarnings("ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values


X = array[:,0:8]
Y = array[:,8]

#feature extraction
model = ExtraTreesClassifier()
model.fit(X,Y) #ginni index
scores = model.feature_importances_
print(scores)

result= list(zip(hnames,scores))
print(result)
print("\n\n")

from operator import itemgetter
print(sorted(result, key=itemgetter(1),reverse=True))

