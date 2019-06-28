import pandas
import urllib.request


hnames = ['sepal-length','sepal-width',
          'petal-length','petal-width','class']
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataframe = pandas.read_csv(web_path, names=hnames)

print( dataframe.shape )
print( dataframe )
print( (dataframe.columns)

