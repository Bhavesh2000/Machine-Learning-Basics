import matplotlib.pyplot as plt
import numpy as np

# evenly sampled numbers at the intervals of .2
t = np.arange(0.0, 5.0, 0.2)
print(t)

# red dashed, blue square, and green triangles
plt.plot(t, t, 'r*-',
         t, t+3, 'bs-',
         t, t+6, 'ro',
         t, t+6, 'g-', markersize='7')  # green coloured line with red dot

plt.show()
