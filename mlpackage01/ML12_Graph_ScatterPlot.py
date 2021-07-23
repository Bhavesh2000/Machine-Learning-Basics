from typing import List

import matplotlib.pyplot as plt

x1 = [2, 3, 5]
y1 = [5, 5, 5]

x2 = [1, 2, 3, 4, 5]
y2 = [2, 3, 2, 3, 4]

x3 = [1, 2, 3, 4, 5]
y3 = [6, 8, 7, 8, 7]

plt.scatter(x1, y1, label='A')

plt.scatter(x2, y2, marker='v', color='r', label='B')
plt.scatter(x3, y3, marker='^', color='m', label='C')

plt.legend(loc="upper left")
plt.title('Scatter Plot Example')
plt.show()