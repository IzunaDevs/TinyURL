# -*- coding: utf-8 -*-
import sys
import urllib
import optparse
from .errors import *
try:
    import asyncio
except ImportError:
    # Well this is bad as this is needed. Maybe not Python 3.4.2+?
    print('Are you running python 3.4.2+? because asyncio looks to be missing.')
    sys.exit(1)
import aiohttp

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


class TinyURL:
    def __init__(self, alias, debug):
        self.loop = asyncio.get_event_loop()
        self.alias = alias
        self.debug = debug
        self.createsession()

    def createsession(self):
        self.session = aiohttp.ClientSession(loop=self.loop)

    @asyncio.coroutine
    def closesession(self):
        if not self.session.close():
            yield from self.session.close()

    @asyncio.coroutine
    def create_one(self, url):
        if url != '' and url is not None:
            if url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'):
                if self.alias is not None:
                    if self.alias != '':
                        url_code = API_CREATE2.format(url, self.alias)
                        with self.session.ws_connect(API_CREATE2) as ws:
                            yield from ws.post(url_code, data=url_code)
                            #ret = urllib.request.urlopen(url_code, data=url_code).read()
                            #result = str(ret).replace("b", "").replace("'", "")
                            result = yield from ws.content.read()
                            yield from ws.close()
                        if self.debug:
                            print(result)
                        yield from self.closesession()
                        return result
                    else:
                        raise InvalidAlias('The given Alias cannot be \'empty\'.')
                else:
                    with self.session.ws_connect(API_CREATE) as ws:
                        yield from ws.post(API_CREATE, data=dict(url=url))
                        #url_data = urllib.parse.urlencode(dict(url=url))
                        #byte_data = str.encode(url_data)
                        #ret = urllib.request.urlopen(API_CREATE, data=byte_data).read()
                        #result = str(ret).replace("b", "").replace("'", "")
                        result = yield from ws.content.read()
                        yield from ws.close()
                    if self.debug:
                        print(result)
                    yield from self.closesession()
                    return result
            else:
                raise InvalidURL('The given URL is invalid.')
        else:
            raise URLError('The given URL Cannot be \'empty\'.')

    @asyncio.coroutine
    def create(self, *urls):
        for url in urls:
            yield from self.create_one(url)

def main(sysargs=sys.argv[:]):
    parser = _build_option_parser()
    opts, urls = parser.parse_args(sysargs[1:])
    loop = asyncio.get_event_loop()
    for url in loop.run_until_complete(TinyURL.create(*urls)):
        sys.stdout.write(url + opts.delimiter)
    return 0


if __name__ == '__main__':
    sys.exit(main())