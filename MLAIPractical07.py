import pandas
filename = 'indians-diabetes.data.csv'


hnames = ['preg','plas','pres','skin','test',
          'mass','pedi','age','class']

dataframe = pandas.read_csv(filename, names=hnames)

print( dataframe.head(20) )
print( "-*-" * 20  )

print( "dataframe.shape : ", dataframe.shape )
print( "-*-" * 20  )
print(dataframe.dtypes )
print( "-#-" * 20  )

pandas.set_option('precision', 2)


print("description = \n", dataframe.describe()  )
print( "-*-" * 20  )

print()

class_counts = dataframe.groupby('class').size()
print( class_counts  )
print( "-#-" * 20  )

correlations = dataframe.corr(method='pearson')
print(  correlations  )



