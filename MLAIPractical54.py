from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")
#plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (8,6)
#importing dataset
data = pd.read_csv('KMeansData.csv')
print("Input Data and Shape")
print(data.shape)
print(data.head()) #first five rows print

#getting values and plotting
f1 = data['V1'].values
f2 = data['V2'].values
plt.scatter(f1, f2, c='black', s=10)
plt.show()


X = np.array(list(zip(f1,f2))) #[[2.072345,-3.241693], [] , []]

#Euclidean distance calculator
def eu_dist(a, b, ax=1):
    return np.linalg.norm(a -b, axis=ax)

#Number of clusters
k = 3
#X coordinates of random centroids
C_x = np.random.randint(0,np.max(X)-20, size=k)
print("C_x=" , C_x)
C_y = np.random.randint(0,np.max(X)-20, size=k)
print("C_y=" , C_y)



C = np.array(list(zip(C_x, C_y)) , dtype= np.float32)
print("Initial Centroids (Random Position) : ")
print(C)
print( C.shape ) #(3,2)


#Plotting along with centroids
plt.scatter(f1,f2, s=10,c='k')
plt.scatter(C_x,C_y, marker='*', s=300,c='r')
plt.show()


#To store the value of centroids when it updates
C_old = np.zeros(C.shape) #C.shape = [3,2]
print("C = \n" , C)
print("C old \n", C_old)

print('len(X) = ', len(X)) #3000

#Cluster Labels(0,1,2)
clusters = np.zeros(len(X))

#zero filled numpy array of 3000 elements
print( "clusters : =", clusters)

#Error func. - distance between new centroids
#and old centroids
error = eu_dist(C,C_old, None)
#loop will run till error becomes zero
while error.all():        #error !=0
    #assigning each value to its closest cluster
    for i in range(len(X)):       #len(X) : 3000
        distances = eu_dist(X[i], C) #dist = from all 3 customer
        cluster = np.argmin(distances) #cluster= 2
        clusters[i] = cluster
    #storing the old centroid values
    C_old = deepcopy(C)
    #Finding the new centroid by taking the avg value
    for i in range(k): #k = 3 because we have to find 3 centroid location
        points = [ X[j] for j in range(len(X)) if clusters[j]==i]
        C[i] = np.mean(points, axis=0)
        error = eu_dist(C, C_old)

colors = ['b','c','r']
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] ==i  ])
    ax.scatter(points[:,0], points[:,1], s=25, c=colors[i])
ax.scatter(C[:,0], C[:,1], marker='*', s=100, c='y')

print("Final Centroid : ", C)
plt.show()





from sklearn.cluster import KMeans
print("KMeans of sk learn")
#number of clusters
kmeans = KMeans(n_clusters=3)

#importing the dataset
data= pd.read_csv('KmeansData.csv')

f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1,f2)))

#Fittiing the input data
kmeans = kmeans.fit(X)

#Getting the cluster labels
labels = kmeans.predict(X)
print( "labels :" , labels)
#Centroid value
centroids = kmeans.cluster_centers_

#Comparing with scikit-learn centroids
print( "KMeans Algo Centroid values :- \n")

print( "KMeans:Manual centroid\n", C)

print("KMeans sklearn:centroids \n ", centroids ) #from scikit-learn