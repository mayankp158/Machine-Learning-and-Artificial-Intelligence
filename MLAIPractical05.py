import pandas

filename = 'indians-diabetes.data.csv'

hnames = ['preg','plas','pres','skin','test',
          'mass','pedi','age','class']
dataframe = pandas.read_csv(filename, names=hnames)

print( "pandas Data : " , dataframe.shape )
print( dataframe )
print( "\n\n" )
print( type(dataframe)  )