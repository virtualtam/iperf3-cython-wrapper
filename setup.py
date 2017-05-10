from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize
import os

EXTENSIONS = [
    Extension(
        'c_iperf3.c_iperf3',
        sources=[os.path.join('c_iperf3', 'c_iperf3.pyx')],
        libraries=['iperf']
    )
]


setup(
    name='iperf3-cython-wrapper',
    version='1.0.0',
    description="IPerf3 Cython wrapper",
    long_description="IPerf3 Cython wrapper",
    ext_modules=cythonize(EXTENSIONS)
)
