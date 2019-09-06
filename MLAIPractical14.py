import numpy as np
a = np.array([1,2,3,4])
print( "a + 1 =", a + 1 )
print( "a = " , a  )
print( "a**2 = ", a ** 2 )

a = np.array([1,2,3,4])
b = np.ones(4) + 1
print( a  )
print( b )
print( "a - b : " , a - b )
print( "a * b : " , a * b )

j = np.arange(5)
print( 2**(j+1)-j)

print("_____________Element wise comparison:___________")

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print( "a==b: ", a == b )
print( "a>b: ", a > b )

print("_____________Array wise comparison_______________")
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
c = np.array([1,2,3,4])
print( "np.array_equal(a,b):") , np.array_equal(a,b)
print( "np.array_equal(a,c):") , np.array_equal(a,c)

print("_____________Logical operations:_________________")
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print("a= ", a )
print("b= ", b)
print( np.logical_or(a,b) )
print( np.logical_and(a,b) )


print( np.pi )


print( np.linspace(-5, 5 , 11)  )
print( np.linspace(-np.pi, np.pi , 256)  )
print( np.linspace(0, 1 , 20)  )

print("_________________Tanscendental functions:_________________")
a = np.arange(1,6)

print( np.sin(a) )

print( np.log(a))
print( np.exp(a))

#Shape mismatch

#a = np.arange(4)
#print( a+ np.array([1, 2])  )#error

#Basic reductions

#Computing sums

x = np.array([1,2,3,4])
print( "np.sum(x) : ", np.sum(x) )
print( "x.sum() : ", x.sum() )

print( "____sum by rows and columns____")

x = np.array([[1,2], [3,4]])
print( "x = \n" , x )

print( x.sum() )

print( x.sum(axis=0) ) #column wise

print( x[:, 0].sum()  , x[:, 1].sum() )

print( x.sum(axis=1) ) #row wise

print( x[0, :].sum()  , x[1, :].sum() )


print("_________Extrema________")
x = np.array([1,3,2])
print( x.min())
print( x.max())


#Logical operations
print( np.all([True,True,False]))
print( np.any([True,True,False]))

print("______Numpy for array comparisons______")
a =  np.zeros((10,10))
print( "a = " , a)
print( np.any(a!=0) )
print( np.all(a==a))

a =np.array([1,2,3,2])
b =np.array([2,2,3,2])
c =np.array([6,4,4,5])
print(((a<=b)& (b <=c)).all())

print("__________Statistics_________")
x = np.array([1,2,3,1,1])

print( "x.mean()=", x.mean() )
print( "np.median()=", np.median(x) )
print( "x.std()=", x.std() )




