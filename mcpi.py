"""
Script that uses the fortran routine for computing pi
and compares run times against a numpy version
"""

from math import sqrt
from numpy import empty_like, array, empty
from functools import wraps
from time import time
from random import random


try:
    from f_mcpi import calc_pi as calc_pi_f90
    from f_mcpi import pi_with_coords
except ImportError:
    raise ImportError(
        "Unable to import fortran module. Have you built it yet?"
    )


def timed(f):
    """Decorator for timing function calls from python"""
    @wraps(f)
    def wrapped(*args, **kwargs):
        start = time()
        out = f(*args, **kwargs)
        end = time()
        return out, end - start
    return wrapped


@timed
def mcpy(n):
    s = 0
    for i in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1:
            s += 1
    return 4 * s / n


@timed
def mcpi_f90(n):
    return calc_pi_f90(n)


def compare_pi(samples):
    bins_py = empty((samples.size, 2), 'd')
    bins_f90 = empty_like(bins_py)
    for i, n in enumerate(samples):
        bins_py[i] = mcpy(n)
        bins_f90[i] = mcpi_f90(n)
    return samples, bins_py.T, bins_f90.T


if __name__ == '__main__':
    from math import pi
    from matplotlib import pyplot
    samples = array([
        100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000
    ]).repeat(3)
    s, bp, bf = compare_pi(samples)
    pyplot.figure()
    pyplot.semilogx(s, bp[0], 'o', label='python')
    pyplot.semilogx(s, bf[0], 'x', label='fortran')
    pyplot.xlabel("Sampled points")
    pyplot.ylabel("Estimated $\\pi$")
    pyplot.axhline(pi, c='r')
    pyplot.legend()

    pyplot.figure()
    pyplot.loglog(s, bp[1] * 1000, 'o', label='python')
    pyplot.loglog(s, bf[1] * 1000, 'x', label='fortran')
    pyplot.xlabel("Sampled points")
    pyplot.ylabel("Run time [ms]")
    pyplot.legend()

    pyplot.figure()
    x, y, pos, _pi = pi_with_coords(1000)
    pyplot.scatter(x, y, c=pos)

    pyplot.show()
