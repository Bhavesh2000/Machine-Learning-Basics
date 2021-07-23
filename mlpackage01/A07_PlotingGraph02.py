import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'cs-', label='line1', linewidth='2')

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-', label='line2', linewidth='4')

# x1 = [1, 2, 3]
# y1 = [1, 2, 3]

# x2 = [1, 2, 3]
# y2 = [1, 4, 9]

# plt.plot(x1, y1, x2, y2, linewidth='7')

plt.axis([0, 6, 0, 26])

plt.legend(loc="upper right")
plt.show()

