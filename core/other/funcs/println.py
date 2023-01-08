from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from sys import stdout


def _println(args: list, env: Environment):
    lenargs(args, 1, "println")
    
    for i, a in enumerate(args):
        if isinstance(a, arrayRepr):
            out = "[" + ", ".join(list(map(lambda x: "'" + x.value + "'" if isinstance(x, stringRepr) else str(x.value), a.value))) + "]"
        else:
            out = str(a.value)
    
    stdout.write(out + "\n")
    
    return None
