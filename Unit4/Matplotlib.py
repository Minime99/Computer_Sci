import matplotlib

matplotlib.pyplot.plot([1, 2, 3, 4])
matplotlib.pyplot.ylabel("some numbers")
matplotlib.pyplot.show()

import numpy
import matplotlib

x = numpy.arange(0, 5, 0.1)
y = numpy.sin(x)
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()
import matplotlib
import numpy


def f(t):
    'A Damped Exponential'
    s1 = numpy.cos(2*numpy.pi*t)
    e1 = numpy.exp(-t)
    return s1*e1


t1 = numpy.arange(0.0, 5.0, .2)

l = matplotlib.pyplot.plot(t1, f(t1), 'ro')
