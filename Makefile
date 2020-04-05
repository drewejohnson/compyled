compare : compare.py all
	./$<

f_mcpi : mcpi.f90
	f2py -c $< -m $@ 

cython : setup_purecython.py purecython.pyx 
	python $< build_ext --inplace

all : f_mcpi cython

clean :
	rm -f f_mcpi.cpython* purecython.cpython* purecython.c
