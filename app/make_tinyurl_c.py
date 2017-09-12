"""
Makes TinyURL.c for an standalone
python application.
"""
import sys
import os


def _write_file(filename, data):
    with open(filename, 'w') as of:
        of.write(data)


def generate_main_py():
    info = """# -*- coding: utf-8 -*-
\"\"\"
Main entrypoint to run TinyURL in
an Embedded Python Interpreter.
\"\"\"
import TinyURL

if __name__ == '__main__':
    TinyURL.main()
"""
    _write_file('__main__.py', info)


def generate_tinyurl_c():
    info = """#include <Python.h>
#ifdef _WIN32
/*
 * for loading python script from the
 * resource section.
 */
#include <windows.h>
#include "resource.h"
#endif

int
main(int argc, char *argv[])
{
  int err;
  wchar_t **argv_copy;
  int i;
  argv_copy = (wchar_t **)PyMem_RawMalloc(sizeof(wchar_t*) * (argc+1));
  if (!argv_copy) {
#ifdef _WIN32
    LPSTR buffer1[28];
    LoadString(GetModuleHandle(NULL), IDS_STRING1, (LPSTR)buffer1, 28);
    fprintf(stderr, (const char *const)buffer1);
#else
    fprintf(stderr, "Fatal error: out of memory\\n");
#endif
    exit(1);
  }
  for (i = 0; i < argc; i++) {
    argv_copy[i] = Py_DecodeLocale(argv[i], NULL);
    if (!argv_copy[i]) {
#ifdef _WIN32
      LPSTR buffer2[61];
      LoadString(GetModuleHandle(NULL), IDS_STRING2, (LPSTR)buffer2, 61);
      fprintf(stderr, (const char *const)buffer2, i + 1);
#else
      fprintf(stderr, "Fatal error: "
                      "unable to decode the command line argument #%i\\n",
                      i + 1);
#endif
      exit(1);
    }
  }
  argv_copy[argc] = NULL;
  Py_SetProgramName(argv_copy[0]);
  Py_Initialize();
  if (Py_IsInitialized() != 0) {
    /*
     * allows use of sys.argv to be possible
     * with no tracebacks.
     */
    PySys_SetArgvEx(argc, argv_copy, 0);
#ifdef _WIN32
    HRSRC script_resource = FindResource(
      NULL, MAKEINTRESOURCE(IDR_RCDATA1), RT_RCDATA);
    unsigned int script_size = SizeofResource(NULL, script_resource);
    HGLOBAL main_script = LoadResource(NULL, script_resource);
    void* pmain_script = LockResource(main_script);
    if (script_size >= 0) {
      err = PyRun_SimpleString((const char *)pmain_script);
    } else {
      LPSTR buffer3[38];
      LoadString(GetModuleHandle(NULL), IDS_STRING3, (LPSTR)buffer3, 38);
      fprintf(stderr, (const char *const)buffer3);
    }
#else
    err = PyRun_SimpleString(\""""
    with open('__main__.py', 'r') as f:
        data = f.read().splitlines()
        for line in data:
            info += line.replace('"', '\\"').replace('\\n', '\\\\n').replace("\\'", "\\\\'")
            info += '\\n"\n                             "'
    info += """\");
#endif
    if (err > 0)
      PyErr_Print();
    Py_Finalize();
  } else {
#ifdef _WIN32
    LPSTR buffer4[41];
    LoadString(GetModuleHandle(NULL), IDS_STRING4, (LPSTR)buffer4, 41);
    fprintf(stderr, (const char *const)buffer4);
#else
    fprintf(stderr, "Fatal error: Python is not initialized.\\n");
#endif
  }
  for (i = 0; i < argc; i++) {
    PyMem_RawFree(argv_copy[i]);
  }
  PyMem_RawFree(argv_copy);
  return 0;
}
"""
    _write_file('TinyURL.c', info)
    if not sys.platform == 'win32':
        os.remove('__main__.py')


def main():
    generate_main_py()
    generate_tinyurl_c()

main()
