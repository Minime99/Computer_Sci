import matplotlib
import matplotlib.pyplot
import numpy
t1 = numpy.arange(0.0, 10.0, 4)
l = matplotlib.pyplot.plot(t1, t1*3, label="goes here")
matplotlib.pyplot.title("here is a title")
matplotlib.pyplot.ylabel("label y")
matplotlib.pyplot.xlabel("label x")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

# when you want to place emphasis on a item
# when you want to show the relationship of individual items to whole picture
# when you want to determine correlation
# when you want toshow trends
