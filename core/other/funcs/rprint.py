from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from sys import stdout


def _rprint(args: list, env: Environment):
    lenargs(args, 1, "rprint")
    
    for i, a in enumerate(args):
        if isinstance(a, arrayRepr):
            out = "[" + ", ".join(list(map(lambda x: "'" + x.value + "'" if isinstance(x, stringRepr) else str(x.value), a.value))) + "]"
        elif isinstance(a, stringRepr):
            out += "'" + str(a.value) + "'"
        else:
            out = str(a.value)
    
    stdout.write("\r{}".format(out))
    
    return None
