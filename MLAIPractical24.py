import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(8,6), dpi=80)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S = np.sin(X)
C = np.cos(X)


plt.plot(X, S, color="red", linewidth=5.0, linestyle="--", label= "sine curve")

plt.plot(X, C, color="blue", linewidth=7.0, linestyle="-", label="cosine curve")

plt.legend(loc ='upper left')

plt.xlim(-4.0, 4.0)

plt.xticks(np.linspace(-4,4,9,endpoint=True))

plt.ylim(-1.0,1.0)
plt.yticks(np.linspace(-1,1,9,endpoint=True))
plt.grid(True)

plt.show()
