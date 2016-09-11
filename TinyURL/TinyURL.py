# -*- coding: utf-8 -*-
import sys
import urllib
import optparse
from .errors import *

API_CREATE = "http://tinyurl.com/api-create.php"
# This is for setting a Alias in a url. This second one is needed (for if you want to customize the shortened url).
API_CREATE2 = "http://tinyurl.com/create.php?source=indexpage&url={0}&submit=Make+TinyURL%21&alias={1}"
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
                    url_code = API_CREATE2.format(url, alias)
                    ret = urllib.request.urlopen(url_code, data=url_code).read()
                    result = str(ret).replace("b", "").replace("'", "")
                    return result
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