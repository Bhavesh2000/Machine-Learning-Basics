import numpy as np
import matplotlib.pyplot as plt

# Plotting with default Setting
X = np.linspace(-np.pi, np.pi, 256, endpoint='True')  # pi=3.14
print('X=', X)

S = np.sin(X)   # sin0=0 and sin90=1
C = np.cos(X)   # cos0=1 and cos90=0

plt.plot(X, S)  # if we supply two lines they will have 2 colours
plt.plot(X, C)
plt.show()
