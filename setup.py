from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = '0.1.1'

if not version:
    raise RuntimeError('version is not set')

readme = 'TinyURL lib for Python 3.x.'

setup(name='TinyURL',
      author='Decorater',
      url='https://github.com/AraHaan/TinyURL', #None for right now till I make a Repo for TinyURL for Python 3.x.
      version=version,
      packages=['TinyURL'],
      license='MIT',
      description='TinyURL for Python 3.x',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.x',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
