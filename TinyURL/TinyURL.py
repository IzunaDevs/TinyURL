# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2015 Decorater

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import optparse
from .errors import *

API_CREATE = "http://tinyurl.com/api-create.php"
# This is for setting a Alias in a url. This second one is needed (for if you want to customize the shortened url).
API_CREATE2 = "http://tinyurl.com/create.php?"
DEFAULT_DELIM = "\n"
USAGE = """%prog [options] url [url url ...]
 
 + __doc__ + 
Any number of urls may be passed and will be returned
in order with the given delimiter, default=%r
 % DEFAULT_DELIM
"""
ALL_OPTIONS = (
    (('-d', '--delimiter'), 
        dict(dest='delimiter', default=DEFAULT_DELIM, 
             help='delimiter for returned results')),
)


def _build_option_parser():
    prs = optparse.OptionParser(usage=USAGE)
    for args, kwargs in ALL_OPTIONS:
        prs.add_option(*args, **kwargs)
    return prs


def create_one(url, alias=None):
    if url != '' and url is not None:
        if url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'):
            if alias is not None:
                if alias != '':
                    payload = {
                        'url': url,
                        'submit': 'Make TinyURL!',
                        'alias': alias
                    }
                    data = urllib.parse.urlencode(payload)
                    full_url = API_CREATE2 + data
                    ret = urllib.request.urlopen(full_url)
                    soup = BeautifulSoup(ret, 'html.parser')
                    check_error = soup.p.b.string
                    if "The custom alias" in check_error:
                        raise AliasUsed('The given Alias you have provided is already bwing used.')
                    else:
                        return soup.find_all('div', {'class': 'indent'})[1].b.string
                else:
                    raise InvalidAlias('The given Alias cannot be \'empty\'.')
            else:
                url_data = urllib.parse.urlencode(dict(url=url))
                byte_data = str.encode(url_data)
                ret = urllib.request.urlopen(API_CREATE, data=byte_data).read()
                result = str(ret).replace("b", "").replace("'", "")
                return result
        else:
            raise InvalidURL('The given URL is invalid.')
    else:
        raise URLError('The given URL Cannot be \'empty\'.')


def create(*urls):
    for url in urls:
        yield create_one(url)


def main(sysargs=sys.argv[:]):
    parser = _build_option_parser()
    opts, urls = parser.parse_args(sysargs[1:])
    for url in create(*urls):
        sys.stdout.write(url + opts.delimiter)
    return 0


if __name__ == '__main__':
    sys.exit(main())