import matplotlib.pyplot
import pylab
import csv
file=open("data.csv", "r")
reader =csv.reader(file)

x = file[0]
y = file[1]

matplotlib.pyplot.scatter(x,y)

matplotlib.pyplot.show()