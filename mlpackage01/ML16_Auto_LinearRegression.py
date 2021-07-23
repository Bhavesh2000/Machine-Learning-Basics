# Finding Price for 700sq.ft. using historic data
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression  # Logistic Regression
warnings.filterwarnings(action="ignore")


def get_data(file_name):
	df = pd.read_csv(file_name)
	print(df)
	X_parameters = []
	Y_parameters = []
	for single_squareFeet, single_priceValue in zip(df['square_feet'], df['price']):
		X_parameters.append([single_squareFeet])
		Y_parameters.append(single_priceValue)
	return X_parameters, Y_parameters


def linear_model_main(X_parameters, Y_parameters, quest_value):
	regr = LinearRegression()
	print("Area: ", X_parameters)
	print("Prices: ", Y_parameters)
	regr.fit(X_parameters, Y_parameters)  # fit=coef_cal m and c for y=mx+c we training the algorithm
	predicted_ans = regr.predict([quest_value])  # predict calculates y_predict
	predictions = {}
	predictions['coefficient'] = regr.coef_
	predictions['intercept'] = regr.intercept_
	predictions['predicted_ans'] = predicted_ans
	print("Output from machine: ", predicted_ans)
	plt.scatter(X_parameters, Y_parameters, color='m', marker='o', s='30')
	all_predicted_Y = regr.predict(X_parameters)
	plt.scatter(X_parameters, all_predicted_Y, color='b')
	plt.plot(X_parameters, all_predicted_Y, color='r')
	plt.scatter(quest_value, predicted_ans, color='g')
	plt.show()
	return predictions


if(__name__ == "__main__"):
	x, y = get_data("LR_House_price.csv")
	question_value = 700  # This is the question
	result = linear_model_main(x, y, question_value)
	print("Coefficient m= ", result['coefficient'])
	print("Intercept value c= ", result['intercept'])
	print("Predicted House Price value: ", result['predicted_ans'])
