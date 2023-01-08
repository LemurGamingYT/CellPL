from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from functools import cache


def _fib(args: list, env: Environment):
    @cache
    def fib(n: int):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    
    lenargs(args, 1, "fib")
    
    return intRepr(fib(args[0].value))
