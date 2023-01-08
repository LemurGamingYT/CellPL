from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *


def _range(args: list, env: Environment):
    lenargs(args, 1, "range")
    
    if not isinstance(args[0], intRepr):
        return report_error("Type", "Range argument one type must be an integer")
    
    return arrayRepr(list(map(lambda x: intRepr(x), list(range(args[0].value)))))
