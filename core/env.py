"""
env.py

handles the environment containing the variables, functions and classes
"""

# import the report_error function to print errors
from .error import report_error


# import the reprs
from .reprs import *


# import the Any variable type
from typing import Any


class Environment():
    def __init__(self):
        self._variables = {}
        self._functions = {}
        self._classes = {}
    
    def exists(self, obj, name: str):
        if obj is None:
            report_error("Unbound", "Unknown object %s" % name)
        else:
            return obj
    
    @property
    def variables(self):
        return self._variables
    
    def get_var(self, name: str):
        return self.exists(self._variables.get(name), name)
    
    def add_var(self, r: varRepr):
        self._variables[r.name] = r
    
    def set_var(self, name: str, new: varRepr):
        self._variables[name] = new
    
    def del_var(self, name: str):
        self._variables.pop(name)
        
    @property
    def functions(self):
        return self._functions
    
    def get_func(self, name: str):
        return self.exists(self._functions.get(name), name)
    
    def add_func(self, r: funcRepr):
        self._functions[r.name] = r
    
    def del_func(self, name: str):
        self._functions.pop(name)
