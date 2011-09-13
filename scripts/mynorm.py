import inspect
import timeit

import numpy as np


v = np.random.random((3,))
print "A single vector:\n", v

def timenorm(norm, number):
    name = inspect.getsource(norm).split("=")[0].strip()
    code = inspect.getsource(norm).split(":")[1].strip()
    setup = "from __main__ import np,v"
    tim = timeit.timeit(code, setup, number=number)
    value = eval("%s(v)" %name)
    print "%s: %.6f time: %.3f code: %s" %(name, value, tim, code)

mynorm1 = lambda v: np.linalg.norm(v)
mynorm2 = lambda v: np.sqrt(np.sum(np.dot(v,v)))
mynorm3 = lambda v: np.sqrt(np.sum(v*v))
mynorm4 = lambda v: np.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])

for mynorm in mynorm1, mynorm2, mynorm3, mynorm4:
    timenorm(mynorm, 5*10**6)

V = np.random.random((1000,3))
print "An array of vectors:\n", V

def timenorms(norm, number):
    name = inspect.getsource(norm).split("=")[0].strip()
    code = inspect.getsource(norm).split(":")[1].strip()
    setup = "from __main__ import np,V"
    tim = timeit.timeit(code, setup, number=number)
    value = eval("%s(V)" %name)[0]
    print "%s: %.6f time: %.3f code: %s" %(name, value, tim, code)

mynorms1 = lambda V: [np.linalg.norm(v) for v in V]
mynorms2 = lambda V: [np.sqrt(sum(v*v)) for v in V]
mynorms3 = lambda V: np.sqrt([sum(v*v) for v in V])
mynorms4 = lambda V: np.sqrt([v[0]*v[0] + v[1]*v[1] + v[2]*v[2] for v in V])
mynorms5 = lambda V: np.sqrt((V*V).sum(axis=1))

for mynorms in mynorms1, mynorms2, mynorms3, mynorms4, mynorms5:
    timenorms(mynorms, 5*10**6/len(V))
