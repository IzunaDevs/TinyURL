"""
Makes TinyURL.c for an standalone
python application.
"""
import sys


def generate_tinyurl_c():
    """
    generates TinyURL.c.
    """
    info = '#include <Python.h>\n'
    info += '#ifdef _WIN32\n'
    info += '/*\n'
    info += '  for loading python script from the\n'
    info += '  resource section.\n'
    info += '*/\n'
    info += '#include <windows.h>\n'
    info += '#include "resource.h"\n'
    info += '#endif\n'
    info += '\n'
    info += 'int\n'
    info += '#ifdef _WIN32\n'
    info += 'wmain(int argc, wchar_t *argv[])\n'
    info += '#else\n'
    info += 'main(int argc, char *argv[])\n'
    info += '#endif\n'
    info += '{\n'
    info += '  int err;\n'
    info += '  wchar_t *program = Py_DecodeLocale(argv[0], NULL);\n'
    info += '  if (program == NULL) {\n'
    info += '    fprintf(stderr, "Fatal error: cannot decode argv[0]\\n");\n'
    info += '    exit(1);\n'
    info += '  }\n'
    info += '  Py_SetProgramName(program);  /* optional but recommended */\n'
    info += '  Py_Initialize();\n'
    info += '  int initialized = Py_IsInitialized();\n'
    info += '  if (initialized != 0) {\n'
    info += '#ifdef _WIN32\n'
    info += '    /*\n'
    info += '      allows use of sys.argv to be possible\n'
    info += '      with no tracebacks.\n'
    info += '\n'
    info += '      Note: This is not possible to use in any other\n'
    info += '      platform for now until someone helps patch\n'
    info += '      this for me (I am not sure what to do to\n'
    info += '      make it work like this on them).\n'
    info += '    */\n'
    info += '    PySys_SetArgvEx(argc, argv, 0);\n'
    info += '    /*\n'
    info += '      For now until I figure out loading the\n'
    info += '      text from resource section.\n'
    info += '    */\n'
    info += '    HRSRC script_resource = FindResource(\n'
    info += '      NULL, MAKEINTRESOURCE(IDR_RCDATA1), RT_RCDATA);\n'
    info += '    unsigned int script_size = SizeofResource(NULL, script_resource);\n'
    info += '    HGLOBAL main_script = LoadResource(NULL, script_resource);\n'
    info += '    void* pmain_script = LockResource(main_script);\n'
    info += '    if (script_size >= 0) {\n'
    info += '      err = PyRun_SimpleString((const char *)pmain_script);\n'
    info += '    } else {\n'
    info += '      /* python script is empty. */\n'
    info += '      fprintf(stderr, "Fatal error: Python script is empty.\\n");\n'
    info += '    }\n'
    info += '#else\n'
    info += '    /* TODO: make PySys_SetArgvEx no crash here to use. */\n'
    info += '    err = PyRun_SimpleString("'
    with open('../TinyURL.py', 'r') as f:
        data = f.read().splitlines()
        for line in data:
            info += line.replace('"', '\\"').replace('\n', '\\n')
            info += '\\n"\n                                 "'
    info += '");\n'
    info += '#endif\n'
    info += '    if (err > 0)\n'
    info += '      PyErr_Print();\n'
    info += '    Py_Finalize();\n'
    # With these 2 lines python 3.5 compile will not be possible.
    # info += '    if (Py_FinalizeEx() < 0)\n'
    # info += '      exit(120);\n'
    info += '  } else {\n'
    info += '    /* python is not initialized. */\n'
    info += '    fprintf(stderr, "Fatal error: Python is not initialized.\\n");\n'
    info += '  }\n'
    info += '  PyMem_RawFree(program);\n'
    info += '  return 0;\n'
    info += '}\n'
    with open('TinyURL.c', 'w') as of:
        of.write(info)


def main():
    generate_tinyurl_c()

main()
