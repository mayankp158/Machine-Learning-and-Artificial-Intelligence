import numpy
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt (web_path, delimiter=",")

for l in dataset :
 print(l)

 print( "Shape of Data from Url : ", dataset.shape )