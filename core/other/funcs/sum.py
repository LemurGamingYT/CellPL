from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *

from functools import reduce


def _sum(args: list, env: Environment):
    lenargs(args, 1, "sum")
    
    if not isinstance(args[0], arrayRepr):
        return report_error("Type", "'sum' takes an array as it's first argument")
    
    return intRepr(sum([s.value for s in args[0].value]))
