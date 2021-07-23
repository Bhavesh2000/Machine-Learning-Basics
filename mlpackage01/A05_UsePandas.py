import pandas
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_column', 9)

filename = "indians-diabetes.data.csv"

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pandas.read_csv(filename, names=hnames) # all data will fill up in df variable
# and hnames(metadata) will on top of top
# if we donot provide metadata then Pandas takes metadata as 1st row of file
print("Pandas data : ", df.shape)

print(df.dtypes) # dtypes gets datatype
print(df)
print(df.describe())
