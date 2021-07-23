import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings(action='ignore')

plt.figure(1)  # the first figure

plt.subplot(311)  # the 1st subplot in the figure
plt.plot([1, 2, 3])  # draw in 1st subplot considered as Y axis coordinates

plt.subplot(312)  # the 2nd subplot in the first figure
plt.plot([4, 5, 6])  # we will draw on 3*2, 2nd subplot in figure 1

plt.subplot(313)  # the 3rd subplot in figure 1
plt.plot([7, 8, 9])  #

plt.figure(2)  # a second figure
plt.plot([11, 12, 13])  # creates a subplot(111) by default

plt.figure(1)  # figure1 current, subplot(313) still current
plt.subplot(311)  # select subplot(311) in figure1
plt.title('Easy as 1, 2, 3')

plt.show()
