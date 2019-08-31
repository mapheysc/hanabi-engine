"""Define user package requirements and various project metadata."""

from setuptools import setup, find_packages

VERSION = '1.0.0'

setup(name='hanaby',
      version=VERSION,
      author='Sam Maphey',
      packages=find_packages(),
      install_requires=[
          'addict',
      ],
      download_url='https://github.com/mapheysc/hanabi-engine/archive/1.0.0.tar.gz'
      )
