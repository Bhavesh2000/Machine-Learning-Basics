import numpy
import urllib.request
# numpy can only read number on cloud. Also we are not getting metadata(data/extra information about data )
# we use pandas as it is an extension numpy
web_path = urllib.request.urlopen(" https://goo.gl/QnHW4g ") # getting data from cloud.
# data is about iris flower getting data its measures and species name

dataset = numpy.genfromtxt(web_path, delimiter=',')

print(dataset)

print("shape of data from url", dataset.shape)