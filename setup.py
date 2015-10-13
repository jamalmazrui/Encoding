from distutils.core import setup
import py2exe

setup(
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "excludes": ["pywin", "pywin.debugger", "pywin.debugger.dbgcon", "pywin.dialogs", "pywin.dialogs.list", "pyreadline", "difflib", "doctest", "optparse", "pickle", "calendar", "pdb", "unittest", "inspect", "Tkconstants", "Tkinter", "tcl"],
                          "bundle_files": 1}},
    zipfile = None,
    version = "1.2",
    description = "File encoding utilities",
    name = "encoding",

    console = ["encoding.py"],
    )
