import inspect
import timeit

from numpy import dot, sqrt, sum
from numpy.linalg import norm
from numpy.random import random
from scipy.spatial.distance import pdist


# Test functions for norm of a single vector.
mynorm1 = lambda v: norm(v)
mynorm2 = lambda v: sqrt(sum(dot(v,v)))
mynorm3 = lambda v: sqrt(sum(v*v))
mynorm4 = lambda v: sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
mynorms = [mynorm1, mynorm2, mynorm3, mynorm4]

# Test functions for lists of vectors.
myNorm1 = lambda V: [norm(v) for v in V]
myNorm2 = lambda V: [sqrt(sum(v*v)) for v in V]
myNorm3 = lambda V: sqrt([sum(v*v) for v in V])
myNorm4 = lambda V: sqrt([v[0]*v[0] + v[1]*v[1] + v[2]*v[2] for v in V])
myNorm5 = lambda V: sqrt((V*V).sum(axis=1))
myNorms = [myNorm1, myNorm2, myNorm3, myNorm4, myNorm5]


if __name__ == "__main__":

    v = random((3,))
    print "A single vector v:"
    print v

    number = 50000
    for i,mynorm in enumerate(mynorms):
        code = inspect.getsource(mynorm).split(":")[1].strip()
        name = "mynorm%i" %(i+1)
        setup = "from __main__ import dot,sqrt,norm,sum"
        tim = timeit.timeit(code, setup, number=number)
        print "%s: %.6f time: %.3f code: %s" %(name, mynorm(v), tim, code)

    V = random((1000,3))
    print "\nAn array of 1000 vectors:"
    print V

    number = 50
    for i,myNorm in enumerate(myNorms):
        code = inspect.getsource(myNorm).split(":")[1].strip()
        name = "myNorm%i" %(i+1)
        setup = "from __main__ import dot,sqrt,norm,sum,V"
        tim = timeit.timeit(code, setup, number=number)
        print "%s: %.6f time: %.3f code: %s" %(name, myNorm(V)[0], tim, code)
    
    print pdist(V,V)[0]
