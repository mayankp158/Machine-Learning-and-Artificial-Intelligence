from matplotlib import pyplot as plt

from pandas import read_csv

from pandas.plotting import scatter_matrix

import warnings
warnings.filterwarnings(action="ignore")

hNames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']

dataframe = read_csv("indians-diabetes.data.csv", names=hNames)

scatter_matrix(dataframe)

plt.show()