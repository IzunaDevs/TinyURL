[![PyPI](https://img.shields.io/pypi/v/TinyURL3.svg)](https://pypi.python.org/pypi/TinyURL3/)
[![PyPI](https://img.shields.io/pypi/pyversions/TinyURL3.svg)](https://pypi.python.org/pypi/TinyURL3/)

The ``TinyURL3`` package provides a few useful functions for 
use from within python code and was modded for ``Python 3.x`` Support.:: 

    >>> import TinyUrl
    >>> TinyUrl.TinyUrl.create_one('http://google.com/')
    'http://tinyurl.com/8kp'
    
    >>> for u in TinyUrl.TinyUrl.create('http://google.com/', 'http://meatballhat.com/'):
    ...    print(u)
    ...
    http://tinyurl.com/8kp
    http://tinyurl.com/7qg8g7


Additionally, a command-line interface is provided for general
use, as in shell scripts or <whatever>... ::

    $ export GOOGLE_URL="`tinyurl http://google.com/`"
    $ echo $GOOGLE_URL
    http://tinyurl.com/8kp

Much love to the folks at `tinyurl.com <http://tinyurl.com>`_!
