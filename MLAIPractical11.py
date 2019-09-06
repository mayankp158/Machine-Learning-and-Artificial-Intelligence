import numpy as np
ddarr = np.array(  [  [1,2] , [3,4,5]  ]  )

print( "ddarr.shape = " , ddarr.shape  )
print( "ddarr.shape = " , ddarr.size  )
print()

d1 = np.array( [ [1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14] ] )

print( d1 )
print( d1.shape )
print( d1.ndim )

print( "d1[: :2,0] = ") , d1[ : :2, 0] #all rows from interval 2
print( "d1[: :2] = ") , d1[ : :2]#all rows on gap of 2
print( d1[1: :2,1] )

zr = np.zeros( [3,4] )
print( "Zero filed array zr = \n" , zr )

ar = np.ones( [4,4] )
print( "1s filed array ar = \n" , ar )

br = np.ones( [6,6] )
print( "6s filed array br = \n" , br * 6 )

print( ar.dtype )

#We can create numpy array from range
ar = np.arange(1,6)
print( "arr = ", ar)

ar[3] = 16
print( "After updating, ar = " , ar  )







