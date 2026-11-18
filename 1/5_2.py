from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("sum_squares.pyx", compiler_directives={'language_level': "3"})
)