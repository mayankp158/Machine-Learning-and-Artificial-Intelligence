import  numpy as np
arr = np.array( [11, 22, 33, 0. ,44, 55] )#one float value will covert other in float in output

print( "arr.sum() = ", arr.sum()  )
print( "arr.std() = ", arr.std()  )
print( "arr.mean() = ", arr.mean()  )
print( "arr.max() = ", arr.max()  )
print( "arr.min() = ", arr.min()  )
print( "arr.size : = ", arr.size  )

#index of non zero value
print( "arr.nonzero() = ", arr.nonzero()  )

print( "arr.dtype= " , arr.dtype )


#are all elements greater than zero
print(np.all([1,2,3,4] )   )
print(np.all([1,2,0,3,4] )  )


#Is any elements non zero
print( np.any( [1,2,3,4]))
print( np.any( [1,2,0,3,4]))
print( np.any( [0,0,0,0.,0]))
print( np.any( [0,0,0,0.,0,1]))


n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print( "\n\n" )
print( "n1  =  " , n1  )
print( "n2  =  " , n2  )
print( "n1 + n2  =  " , n1 + n2  )
print( "n1 - n2 =  " , n1 - n2  )


n3 = np.array([4,5,6,7])
#print( n1 + n3 ) #error


