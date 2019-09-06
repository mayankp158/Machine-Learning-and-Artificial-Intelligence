import  numpy as np

print( "______________________________")
ddarr = np.array( [ [1,2,3],
                    [4,5,6] ] )

print( "ddarr.ndim = " , ddarr.ndim ) #dimension

print( "ddarr.shape = " , ddarr.shape[0] ) #remove[0] to show tuples(structure format)

print( "ddarr.size = " , ddarr.size ) #number of values

print( "ddarr.dtype = " , ddarr.dtype )

print (ddarr)

print("*************************************************************")
print("ddarr[0,1] = " , ddarr[0,1]) #before , row after column
print("ddarr[0] = " , ddarr[0])

print("ddarr[:,0] = " , ddarr[:,0]) #from all rows take column0
print("ddarr[1,:] = " , ddarr[1,:])#row 1 all columns

