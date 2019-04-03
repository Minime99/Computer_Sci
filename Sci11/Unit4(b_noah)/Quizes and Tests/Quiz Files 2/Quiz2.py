import matplotlib
import matplotlib.pyplot
import numpy

t1 = numpy.arange(0.0, 10.0, .2)
l = matplotlib.pyplot.plot(t1, 3**t1+4, label = 'LABEL GOES HERE')
matplotlib.pyplot.title('THIS IS THE TITLE')
matplotlib.pyplot.ylabel('Y AXIS LABEL')
matplotlib.pyplot.xlabel('X AXIS LABEL')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


#1. Line 7 Adds title
#2. Line 8 Labels Y axis
#2. Line 9 Labels X axis
#3. (label = 'LABEL GOES HERE') in line 6 designates what is in the legend. Line 10 shows the legend
#4. When you want to place emphasis on an item
#5. When you want to compare certain parts of a whole
#6. When you want to uneven intervals or data clusters.
#7. When you want to show trends
