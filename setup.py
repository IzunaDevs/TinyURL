from setuptools import setup

requirements = []
# since v0.1.6 this requires beautifulsoup4.
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except Exception as ex:
    with open('TinyURL3.egg-info\requires.txt') as f:
        requirements = f.read().splitlines()

version = '0.1.8'

if not version:
    raise RuntimeError('version is not set')

with open('README.md') as f:
    readme = f.read()

setup(name='TinyURL3',
      author='Decorater',
      author_email='seandhunt_7@yahoo.com',
      url='https://github.com/AraHaan/TinyURL',
      bugtrack_url='https://github.com/AraHaan/TinyURL/issues',
      version=version,
      packages=['TinyURL'],
      license='MIT',
      description='TinyURL for Python 3.x',
      long_description=readme,
      maintainer_email='seandhunt_7@yahoo.com',
      download_url='https://github.com/AraHaan/TinyURL',
      include_package_data=True,
      install_requires=requirements,
      platforms='Any',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.x',
        'Programming Language :: Python :: 3.x',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
