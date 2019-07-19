import importlib
import logging
import pkgutil
import sys
import os
import sources.undp

description = ""
url = ""

MainModule = "__init__"

sourceslist = {}
folder = "sources"
folders = []

path = os.path.join(os.path.dirname(__file__), "sources")

sys.path.append(path)

modules = pkgutil.iter_modules(path=[path])

for loader, mod_name, ispkg in modules:

    if ispkg == True:
        module = loader.find_module(mod_name).load_module(mod_name)
        exec('%s = module' % mod_name)
