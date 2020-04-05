from libc.stdlib cimport rand, RAND_MAX
from libc.math cimport sqrt as c_sqrt

def mcpi(int n):
    cdef double x, y
    cdef int inside, i, draw
    cdef D_RAND_MAX=<double>RAND_MAX
    inside = 0
    for i in range(n):
        x = <double>rand() / D_RAND_MAX
        y = <double>rand() / D_RAND_MAX
        if c_sqrt(x*x + y*y) <= 1:
            inside += 1
    return 4*<double>inside / <double>n
