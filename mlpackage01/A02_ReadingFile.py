# 1.Load csv(comma seperated values) using Python Standard Library.
# there's also another tsv(Tab seperated data). also their is JSON format
# This is not used because of operational broadcasting.
# It converts data in string formate also we can
import csv
fileName = open('indians-diabetes.data.csv', 'r')
reader = csv.reader(fileName, delimiter=',')  # from where to read and delimeter is 'comma' that's why we use "csv".

lines = list(reader)
print("\n\nNo of rows:", len(lines), "\n\n")

print(lines)  # while we read list of list is created.

print("\n\n")
for li in lines:
	print(li)
