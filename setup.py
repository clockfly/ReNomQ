import os
import sys
import re
import shutil
import pathlib
import numpy
from setuptools import setup, find_packages, Extension
import distutils.command.build
from Cython.Build import cythonize
from distutils.extension import Extension


if sys.version_info < (3, 4):
    raise RuntimeError('renom_q requires Python3')

DIR = str(pathlib.Path(__file__).resolve().parent)

setup(
    name="renom_q",
    version="0.1b1",
    packages=['renom_q'],
    include_package_data=True,
    zip_safe=True,
    install_requires=["qiskit"],
)
