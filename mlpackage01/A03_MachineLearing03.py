# it is mostly used
# it converts data into float number

import numpy


data = numpy.loadtxt('indians-diabetes.data.csv',  delimiter=',')


print("numpy loadtext: ", data.shape)

print('\n\n')
print(data)
