# compyled
Play around with `f2py` and other ways to use compiled code (fortran, c) with python

## Content

1. `mcpi.f90` - routines for estimating the value of pi using the Monte Carlo method
2. `purecython.pyx` - pure cython implementation with a corresponding setup file

## Setup

A very basic Makefile is provided that will compile the fortran and cython modules and run the comparison after
running the ``make`` command. 

## Estimating pi using Monte Carlo

Here, we use the Monte Carlo method of drawing random numbers to estimate pi. `N` random `(x, y)` 
pairs are drawn with values between 0 and 1. We take the number of points inside the square as a 
proxy for the area of the square. We also compute the number of points inside a circle of radius one, with 
`sqrt(x ^ 2 + y ^ 2) <= 1` as a proxy for the area of the circle. Since we are only looking at values of 
`x` and `y` that are positive, we are estimating a quarter of the area. 

The value of pi can be estimated by taking a ratio of the areas:

`A_circle / A_square = pi * R^2 / (4 * 1) = pi / 4 ~ N_inside / N`

`pi ~ 4 * N_inside / N`

The figure below presents a plot of 1000 random points drawn inside this unit square. The yellow points are 
inside the disk, while the purple points are outside the disk.

![Visualization of random points inside unit square and sphere](https://raw.githubusercontent.com/drewejohnson/compyled/master/figs/pi_coords.png)

By increasing the number of points drawn, the area of the circle is better approximated, and thus the guess improves.

![Convergence of estimated pi over number of points sampled](https://raw.githubusercontent.com/drewejohnson/compyled/master/figs/pi_value.png)

The two plots above were generated using the [`compare.py`](https://github.com/drewejohnson/compyled/blob/master/compare.py) 
python script. This script relies upon the fortran subroutine 
[`pi_with_coords`](https://github.com/drewejohnson/compyled/blob/39fdcc64f74f90032c50a73165e8be7df5bfbfa0/mcpi.f90#L3). 
The estimates are computed using implementations in
- pure python
- [`cython`](https://cython.org/)
- fortran wrapped with [`f2py`](https://docs.scipy.org/doc/numpy/f2py/)

### But why?

That's a fair question. We can see from the above picture that the methods both appear to be decently accurate 
and converge at about the same rate. So why is this hybrid approach necessary?

Python is slow.

...er than compiled code

![Run time for python and fortran when computing pi](https://raw.githubusercontent.com/drewejohnson/compyled/master/figs/pi_runtime.png)

Even for this simple exercise, the compiled fortran is about 10-times faster when many many points are used. 
This is largely due to the benefits received from a compiled, statically-typed language rather than an interpreted, 
dynamically-typed program. Rather than rehash what many people on the internet have said, links are provided.

1. [Wikipedia - Compiled language](https://en.wikipedia.org/wiki/Compiled_language)
1. [Wikipedia - Interpreted language](https://en.wikipedia.org/wiki/Interpreted_language)
1. [SO - What is the difference between statically typed and dynamically typed languages?](https://stackoverflow.com/q/1517582)
