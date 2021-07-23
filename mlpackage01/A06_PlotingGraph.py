# b- = Blue Slide Line
# ro = Red Circle Dot, have more colours as 'm'-magenta, 'k'-black and marks as 'o'-circle, 's'-square, etc.

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4]) # it takes values of y axis default if we did not pass
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'cs-')
plt.xlabel('Some no. x')
plt.ylabel('squared values')
plt.axis([0, 5, 0, 17])  # limit of x and y axes

plt.show()

# x=[0, 1, 2, 3] index of y-array is taken
# we can get multiple plots.
