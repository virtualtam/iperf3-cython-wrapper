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
    ext_modules=cythonize(EXTENSIONS),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
