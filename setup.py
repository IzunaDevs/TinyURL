from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = '0.1.4'

if not version:
    raise RuntimeError('version is not set')

readme = 'TinyURL lib for Python 3.x.'

setup(name='TinyURL3',
      author='Decorater',
      url='https://github.com/Cheeselab/TinyURL',
      version=version,
      packages=['TinyURL'],
      license='MIT',
      description='TinyURL for Python 3.x',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry ',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
