import numpy as np
n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])

print( n4)
n4.sort() #in-place sorting
print( "After n4.sort() = " , n4 )

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])

print( "n4  =   :", n4 )
print( "n4.argsort():", n4.argsort()  )
print( "n4  =   : ", n4 )

for i in n4.argsort() : #print index in ascending order
    print( n4[i] , end=" " )

print( n4[ n4.argsort() ] ) #original values in n4
print( "n4 = ", n4 )

na= np.array([[1,2,3],[4,5,6]])
print( "na = \n" , na )
print( "na.transpose() = \n", na.transpose() )
print( "na = \n" , na )

print( "identity matrix = \n" , np.eye(6) )

a = np.ones([3,3])
a = a * 3
a[2,2] = 7
I = np.eye(3)
b = np.dot(a,I) #matrix multiplication

print( a)
print()
print( I )
print
print( b )

na= np.array([[1,2],[5,6]])
print( "na = \n" , na )
print( "____________________________________")
print( np.dot(na , na) )
