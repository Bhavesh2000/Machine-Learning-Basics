# Pie Chart
# Supervised ML 1)Regression/Linear (Contineous o/p ) 2)Classification/Logistic regression(Discreate o/p)
# Unsupervised 1)Clustering(Grouping) by K-Means Algo.
import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
	n = np.size(x)

	# calculating mean
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating dy and dx for slope
	SS_xy = np.sum(x * y) - (n * m_x * m_y)
	SS_xx = np.sum(x * y) - (n * m_x * m_x)

	# calculating regression
	m = SS_xy/SS_xx
	c = m_y - (m*m_x)  # c= y - mx
	return[m, c]


def plot_regression_line(x, y, b):  # m=b[1] and c=b[0]

	plt.scatter(x, y, color='m', marker='o', s=39)
	# predicted response vector
	y_prep = (b[1] * x) + b[0]
	# s= 1/
	# plotting regression line
	plt.scatter(x, y_prep, color='g')
	plt.plot(x, y_prep, color='b')
	# putting labels
	plt.xlabel("----X------")
	plt.ylabel("----Y------")
	# function to show
	plt.show()


def startAIAlgorithm():
	# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	# y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
	x = np.array([150, 200, 250, 300, 350, 400, 600])
	y = np.array([6450, 7450, 8450, 9450, 11450, 15450, 18450])
	# estimating co-efficient
	m, c = estimate_coef(x, y)
	print("Estimated Coefficient:\n")
	print("slope m:", m)
	print("y intercept c:", c)
	print("y = ", m, "*x+", c)
	# plotting regression line
	plot_regression_line(x, y, [c, m])


if(__name__ == "__main__"):
	startAIAlgorithm()
# drawback
# 1)Historic data and ML logic in same code file
# 2)All calculation done manually
# 3)Model not applied for future prediction
