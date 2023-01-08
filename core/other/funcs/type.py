from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *


def _type(args: list, env: Environment):
    lenargs(args, 1, "type")
    
    if not isinstance(args[0], idRepr):
        return report_error("Type", "'type' requires a variable argument")
    else:
        return stringRepr(env.get_var(args[0].value).vartype)
