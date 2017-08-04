import sys

from setuptools import setup, find_packages

print("XXX", sys.executable)


setup(name="testpipinstall",
      packages=find_packages())
