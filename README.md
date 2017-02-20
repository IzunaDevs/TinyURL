[![PyPI](https://img.shields.io/pypi/v/TinyURL3.svg)](https://pypi.python.org/pypi/TinyURL3/)
[![PyPI](https://img.shields.io/pypi/pyversions/TinyURL3.svg)](https://pypi.python.org/pypi/TinyURL3/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/96b57a1e85ee438da862574637aaec3c)](https://www.codacy.com/app/AraHaan/TinyURL?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AraHaan/TinyURL&amp;utm_campaign=Badge_Grade)

The ``TinyUrl`` package provides a few useful functions for 
Modded for ``Python 3.x`` Support.
use from within python code:: 

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

.. vim:filetype=rst
