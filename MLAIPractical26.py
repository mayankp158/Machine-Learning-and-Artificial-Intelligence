import numpy as np
import pandas as pd #print data and meta data

s = pd.Series([1,3, np.nan,15,7,8])
print(s)

dates = pd.date_range('20180101',periods=6,freq='D')
print(dates)

print(dates[0])

print(np.random.randn(6,4))


df = pd.DataFrame(np.random.randn(6,4),  #pandas matrix is dataframe
        index= dates,
        columns= ['A','B','C' , 'D']
                  )
print(df)

print("Headings in Dataframe : " , df.columns)
print("Row Headings in Dataframe : " , df.index)
print("Values in Dataframe : " , df.values)

df2 = pd.DataFrame({  'A' : 1.0,
                      'B' : pd.Timestamp("20190102121400"),
                      'C' : pd.Series(1,index=list(range(4)),dtype='float64'),
                      'D' : np.array(  [3]  *  4,  dtype='int64'),
                      'E' : pd.Categorical(["test", "train","train", "test"],
                                           categories=["test","train"]),
                      'F' : 'foo'
                      }
                   )
print(df2)
print(df2.dtypes)

print(df.head()) #print top 5 rows

print(df.tail()) #print last 5 rows
print(df.sample(3)) #print random rows
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())

print(df.describe(include="all")) #for non numeric
print(df.T) #transposing

print("original values : \n ", df)
print("Sorted values : \n" , df.sort_values(by='B',ascending=True))


print("original values : \n", df )

#selecting single cloumn, which yields a series, equivalent to df.A
print( df.A )
print()
print( df['A'] )

print(df['2018-01-01':'2018-01-03'])

#selecting via[] which slice of row
print(df[0:3])#print first three rows #ending is excluded in indexing

print( df.loc[dates[0]])
print(df.loc[:,['A','B']])

print(df.loc['20180102':'20180104',['A','B']])

print(df.loc['20180102',['A','B']])

print( df.loc[dates[0],'A']) #getting scalar value

print(df.at[dates[0], 'A']) #getting faster access to a scalar value

print("/n")
print(df.iloc[3])

print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4] , [0,2]])

print(df.iloc[1:3,:])
print(df.iloc[:,1:3])

print(df.iloc[1,1])

print(df.iat[1,1])

print("\n\n\n")
#Boolean indexing
print(df.A)

print("\n\n")
print(df.A > 0)
print("\n\n")
print(df[df.A > 0])

print("\n\n")
print(df["B"][df.A>0])

print("\n\n")
print(df>0)

print("\n\n")
print(df[df >0])

df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

print( df2[ df2['E'].isin(['two','four'])] )

print(df.mean())

print("\n\nMean of B : " , df.B.mean())
print("\n\nMean of B : " , df['B'].mean())

print(df[df.B > df.B.mean()])


print(df.mean(axis=1))

print("\n\nAfter deletion \n")
print(df2.drop(df2.index[2:4],axis=0))

print("\n\nAfter deletion \n")
print(df2.drop(df2.columns[1:3],axis=1))

print("\n\n")
print(df2)

df.to_excel('outputData.xlsx', sheet_name='Sheet1')



