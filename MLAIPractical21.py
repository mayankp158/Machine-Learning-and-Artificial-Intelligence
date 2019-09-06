import matplotlib.pyplot as plt
import numpy as np

#evenly shaped time at 200ms intervals
t = np.arange(0.0,5.0,0.2)

print(t)

#red dashes,blue squares and green triangles
plt.plot(t,t,'r*-', t, t+3,'bs-',
         t,t+6,'ro',t,t+6,'b-', markersize=5 )

plt.show()