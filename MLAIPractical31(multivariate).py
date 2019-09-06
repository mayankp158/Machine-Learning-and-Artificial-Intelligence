import warnings
warnings.filterwarnings(action="ignore")

from matplotlib import pyplot as plt
import pandas as pd
import numpy

hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi','age', 'class']

dataframe = pd.read_csv('indians-diabetes.data.csv', names = hnames)
correlations = dataframe.corr()

print(correlations)

#plot correlation
fig = plt.figure()

#add matrix and side bar in entire area
subFig = fig.add_subplot(111)

cax = subFig.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)

#------------------------

ticks = numpy.arange(0,9)
subFig.set_xticks(ticks)
subFig.set_yticks(ticks)
subFig.set_xticklabels(hnames)
subFig.set_yticklabels(hnames)

#------------------------

plt.show()