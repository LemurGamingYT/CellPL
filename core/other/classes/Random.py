from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from random import randint, choice

class Random():
    @staticmethod
    def rint(args: list, env: Environment):
        lenargs(args, 2, "Random.rint")
        
        if not isinstance(args[0], intRepr):
            return report_error("Type", "Argument one for 'Random.rint' should be an integer")
        
        if not isinstance(args[1], intRepr):
            return report_error("Type", "Argument two for 'Random.rint' should be an integer")
        
        return intRepr(randint(args[0].value, args[1].value))
    
    @staticmethod
    def rarray(args: list, env: Environment):
        lenargs(args, 1, "Random.rarray")
        
        if not isinstance(args[0], arrayRepr):
            return report_error("Type", "'Random.rarray' first argument must be an array")
        
        return choice(args[0].value)
