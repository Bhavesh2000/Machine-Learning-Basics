import matplotlib.pyplot as plt

idxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr1 = [23, 40, 28, 43, 8, 44, 43, 18, 17]
arr2 = [17, 30, 22, 14, 17, 17, 29, 22, 30]
arr3 = [15, 31, 18, 22, 18, 19, 13, 32, 39]

plt.stackplot(idxes, arr1, arr2, arr3, colors=['r', 'g', 'b'])

plt.legend(['D11', 'D12', 'D13'], loc="best")

plt.title("Stack Plot Example")

plt.show()
