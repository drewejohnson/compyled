from setuptools import Extension, setup
from Cython.Build import cythonize

purecython = Extension("purecython", ["purecython.pyx"])

setup(
    ext_modules=cythonize(
        [purecython],
        compiler_directives={"language_level": 3},
    ),
)
