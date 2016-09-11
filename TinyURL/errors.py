# -*- coding: utf-8 -*-


class TinyURLErrors(Exception):
    pass

class URLError(TinyURLErrors):
    pass

class InvalidURL(TinyURLErrors):
    pass
