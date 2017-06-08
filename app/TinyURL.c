#include <Python.h>
#ifdef _WIN32
/*
  for loading python script from the
  resource section.
*/
#include <windows.h>
#include "resource.h"
#endif

int
#ifdef _WIN32
wmain(int argc, wchar_t *argv[])
#else
main(int argc, char *argv[])
#endif
{
  int err;
  wchar_t *program = Py_DecodeLocale(argv[0], NULL);
  if (program == NULL) {
    fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
    exit(1);
  }
  Py_SetProgramName(program);  /* optional but recommended */
  Py_Initialize();
  int initialized = Py_IsInitialized();
  if (initialized != 0) {
#ifdef _WIN32
    /*
      allows use of sys.argv to be possible
      with no tracebacks.

      Note: This is not possible to use in any other
      platform for now until someone helps patch
      this for me (I am not sure what to do to
      make it work like this on them).
    */
    PySys_SetArgvEx(argc, argv, 0);
    /*
      For now until I figure out loading the
      text from resource section.
    */
    HRSRC script_resource = FindResource(
      NULL, MAKEINTRESOURCE(IDR_RCDATA1), RT_RCDATA);
    unsigned int script_size = SizeofResource(NULL, script_resource);
    HGLOBAL main_script = LoadResource(NULL, script_resource);
    void* pmain_script = LockResource(main_script);
    if (script_size >= 0) {
      err = PyRun_SimpleString((const char *)pmain_script);
    } else {
      /* python script is empty. */
      fprintf(stderr, "Fatal error: Python script is empty.\n");
    }
#else
    /* TODO: make PySys_SetArgvEx must not crash here to use. */
    #error "PySys_SetArgvEx must not crash here to use for this platform."
    err = PyRun_SimpleString("# -*- coding: utf-8 -*-\n"
                                 "\"\"\"\n"
                                 "The MIT License (MIT)\n"
                                 "\n"
                                 "Copyright (c) 2015-2017 Decorater\n"
                                 "\n"
                                 "Permission is hereby granted, free of charge, to any person obtaining a\n"
                                 "copy of this software and associated documentation files (the \"Software\"),\n"
                                 "to deal in the Software without restriction, including without limitation\n"
                                 "the rights to use, copy, modify, merge, publish, distribute, sublicense,\n"
                                 "and/or sell copies of the Software, and to permit persons to whom the\n"
                                 "Software is furnished to do so, subject to the following conditions:\n"
                                 "\n"
                                 "The above copyright notice and this permission notice shall be included in\n"
                                 "all copies or substantial portions of the Software.\n"
                                 "\n"
                                 "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS\n"
                                 "OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
                                 "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
                                 "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
                                 "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING\n"
                                 "FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\n"
                                 "DEALINGS IN THE SOFTWARE.\n"
                                 "\"\"\"\n"
                                 "import sys\n"
                                 "try:\n"
                                 "    import urllib.request\n"
                                 "    import urllib.parse\n"
                                 "except ImportError:\n"
                                 "    import urllib\n"
                                 "from bs4 import BeautifulSoup\n"
                                 "import optparse\n"
                                 "import re\n"
                                 "try:\n"
                                 "    parse_helper = urllib.parse\n"
                                 "except AttributeError:\n"
                                 "    parse_helper = urllib\n"
                                 "try:\n"
                                 "    request_helper = urllib.request\n"
                                 "except AttributeError:\n"
                                 "    request_helper = urllib\n"
                                 "\n"
                                 "\n"
                                 "class errors:\n"
                                 "    \"\"\"\n"
                                 "    Holds all error Classes.\n"
                                 "    \"\"\"\n"
                                 "\n"
                                 "    class TinyURLErrors(Exception):\n"
                                 "        \"\"\"\n"
                                 "        Base Exception Class.\n"
                                 "        \"\"\"\n"
                                 "        pass\n"
                                 "\n"
                                 "    class URLError(TinyURLErrors):\n"
                                 "        \"\"\"\n"
                                 "        For URL Errors.\n"
                                 "        \"\"\"\n"
                                 "        pass\n"
                                 "\n"
                                 "    class InvalidURL(TinyURLErrors):\n"
                                 "        \"\"\"\n"
                                 "        For Invalid URL's.\n"
                                 "        \"\"\"\n"
                                 "        pass\n"
                                 "\n"
                                 "    class InvalidAlias(TinyURLErrors):\n"
                                 "        \"\"\"\n"
                                 "        For Invalid Aliases.\n"
                                 "        \"\"\"\n"
                                 "        pass\n"
                                 "\n"
                                 "    class AliasUsed(TinyURLErrors):\n"
                                 "        \"\"\"\n"
                                 "        For already used Aliases.\n"
                                 "        \"\"\"\n"
                                 "        pass\n"
                                 "\n"
                                 "\n"
                                 "API_CREATE_LIST = [\n"
                                 "    \"http://tinyurl.com/api-create.php\",\n"
                                 "    \"http://tinyurl.com/create.php?\"]\n"
                                 "DEFAULT_DELIM = \"\\n\"\n"
                                 "USAGE = \"\"\"%prog [options] url [url url ...]\n"
                                 " \n"
                                 " + __doc__ + \n"
                                 "Any number of urls may be passed and will be returned\n"
                                 "in order with the given delimiter, default=%r\n"
                                 " % DEFAULT_DELIM\n"
                                 "\"\"\"\n"
                                 "pattern = \"(arp|dns|dsn|imap|http|sftp|ftp|icmp|idrp|ip|irc|pop3|par|rlogin\"\n"
                                 "pattern += \"|smtp|ssl|ssh|tcp|telnet|upd|up|file|git)(s?):\/\/[\/]?\"\n"
                                 "\n"
                                 "ALL_OPTIONS = ((('-d', '--delimiter'), dict(\n"
                                 "    dest='delimiter', default=DEFAULT_DELIM,\n"
                                 "    help='delimiter for returned results')),)\n"
                                 "\n"
                                 "\n"
                                 "def _build_option_parser():\n"
                                 "    prs = optparse.OptionParser(usage=USAGE)\n"
                                 "    for args, kwargs in ALL_OPTIONS:\n"
                                 "        prs.add_option(*args, **kwargs)\n"
                                 "    return prs\n"
                                 "\n"
                                 "\n"
                                 "def create_one(url, alias=None):\n"
                                 "    \"\"\"\n"
                                 "    Shortens a URL using the TinyURL API.\n"
                                 "    :param url: URL.\n"
                                 "    :param alias: Alias.\n"
                                 "    :return: Shortened URL.\n"
                                 "    \"\"\"\n"
                                 "    if url != '' and url is not None:\n"
                                 "        regex = re.compile(pattern)\n"
                                 "        searchres = regex.search(url)\n"
                                 "        if searchres is not None:\n"
                                 "            if alias is not None:\n"
                                 "                if alias != '':\n"
                                 "                    payload = {\n"
                                 "                        'url': url,\n"
                                 "                        'submit': 'Make TinyURL!',\n"
                                 "                        'alias': alias\n"
                                 "                    }\n"
                                 "                    data = parse_helper.urlencode(payload)\n"
                                 "                    full_url = API_CREATE_LIST[1] + data\n"
                                 "                    ret = request_helper.urlopen(full_url)\n"
                                 "                    soup = BeautifulSoup(ret, 'html.parser')\n"
                                 "                    check_error = soup.p.b.string\n"
                                 "                    if 'The custom alias' in check_error:\n"
                                 "                        raise errors.AliasUsed(\n"
                                 "                            \"The given Alias you have provided is already\"\n"
                                 "                            \" being used.\")\n"
                                 "                    else:\n"
                                 "                        return soup.find_all(\n"
                                 "                            'div', {'class': 'indent'}\n"
                                 "                            )[1].b.string\n"
                                 "                else:\n"
                                 "                    raise errors.InvalidAlias(\n"
                                 "                        \"The given Alias cannot be 'empty'.\")\n"
                                 "            else:\n"
                                 "                url_data = parse_helper.urlencode(dict(url=url))\n"
                                 "                byte_data = str.encode(url_data)\n"
                                 "                ret = request_helper.urlopen(\n"
                                 "                    API_CREATE_LIST[0], data=byte_data).read()\n"
                                 "                result = str(ret).replace('b', '').replace(\"\\'\", '')\n"
                                 "                return result\n"
                                 "        else:\n"
                                 "            raise errors.InvalidURL(\"The given URL is invalid.\")\n"
                                 "    else:\n"
                                 "        raise errors.URLError(\"The given URL Cannot be 'empty'.\")\n"
                                 "\n"
                                 "\n"
                                 "def create(*urls):\n"
                                 "    \"\"\"\n"
                                 "    Shortens URL's\n"
                                 "    :param urls: Url list.\n"
                                 "    :return: Shortened URL's\n"
                                 "    \"\"\"\n"
                                 "    for url in urls:\n"
                                 "        yield create_one(url)\n"
                                 "\n"
                                 "\n"
                                 "def main(sysargs=sys.argv[:]):\n"
                                 "    \"\"\"\n"
                                 "    Entry Point.\n"
                                 "    :param sysargs: Args.\n"
                                 "    :return: Nothing.\n"
                                 "    \"\"\"\n"
                                 "    parser = _build_option_parser()\n"
                                 "    opts, urls = parser.parse_args(sysargs[1:])\n"
                                 "    try:\n"
                                 "        for url in create(*urls):\n"
                                 "            sys.stdout.write(url + opts.delimiter)\n"
                                 "    except Exception as ex:\n"
                                 "        print(\"Error: \" + str(ex))\n"
                                 "\n"
                                 "\n"
                                 "__title__ = 'TinyURL'\n"
                                 "__author__ = 'Decorater'\n"
                                 "__license__ = 'MIT'\n"
                                 "__copyright__ = 'Copyright 2015-2017 Decorater'\n"
                                 "__version__ = '0.1.10'\n"
                                 "__build__ = 0x0001010\n"
                                 "\n"
                                 "\n"
                                 "if __name__ == '__main__':\n"
                                 "    sys.dont_write_bytecode = True\n"
                                 "    main()\n"
                                 "");
#endif
    if (err > 0)
      PyErr_Print();
    Py_Finalize();
  } else {
    /* python is not initialized. */
    fprintf(stderr, "Fatal error: Python is not initialized.\n");
  }
  PyMem_RawFree(program);
  return 0;
}
