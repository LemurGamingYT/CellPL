from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from math import sqrt, sin, cos, pi


class Math():
    @staticmethod
    def sine(args: list, env: Environment):
        lenargs(args, 1, "Math.sine")
        
        if not isinstance(args[0], (intRepr, floatRepr)):
            return report_error("Type", "'Math.sine' takes 1 type 'int' or 'float' argument")

        return floatRepr(sin(args[0].value))
    
    @staticmethod
    def cosine(args: list, env: Environment):
        lenargs(args, 1, "Math.cosine")
        
        if not isinstance(args[0], (intRepr, floatRepr)):
            return report_error("Type", "'Math.cosine' takes 1 type 'int' or 'float' argument")

        return floatRepr(cos(args[0].value))
    
    @staticmethod
    def squareroot(args: list, env: Environment):
        lenargs(args, 1, "Math.squareroot")
        
        if not isinstance(args[0], (intRepr, floatRepr)):
            return report_error("Type", "'Math.squareroot' takes 1 type 'int' or 'float' argument")

        return floatRepr(sqrt(args[0].value))
