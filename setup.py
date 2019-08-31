"""Define user package requirements and various project metadata."""

from setuptools import setup, find_packages
import hanabi

VERSION = hanabi.__VERSION__

setup(name='hanaby',
      version=VERSION,
      author='Sam Maphey',
      packages=find_packages(),
      install_requires=[
          'addict',
      ],
      download_url='https://github.com/mapheysc/hanabi-engine/archive/1.0.0.tar.gz'
      )
