from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name='peakonly',
    packages=find_packages(),
    ext_modules=cythonize('cython_utils/roi.pyx'),
    include_dirs=[np.get_include()]
)
