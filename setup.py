"""Define user package requirements and various project metadata."""

from setuptools import setup, find_packages

VERSION = __import__('hanabi').__VERSION__

setup(name='hanabi',
      version=VERSION,
      author='Sam Maphey',
      packages=find_packages(),
      )
