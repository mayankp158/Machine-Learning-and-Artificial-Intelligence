import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(311)

plt.plot([1,2,3]) #(0,1) (1,2) (2,3) data points

plt.subplot(312)
plt.plot([4,5,6])

plt.subplot(313)
plt.plot([7,8,9])

plt.figure(2)
plt.plot([11,12,13])

plt.figure(1)
plt.subplot(311)
plt.title('Easy as 1,2,3')
plt.show()