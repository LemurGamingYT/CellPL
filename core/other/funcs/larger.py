from ...error import report_error
from ..lengthargs import lenargs
from ...env import Environment
from ...reprs import *


def _larger(args: list, env: Environment):
    lenargs(args, 2, "larger")
    
    if not isinstance(args[0], intRepr) or not isinstance(args[1], intRepr):
        return report_error("Type", "'larger' needs both arguments to be type 'int'")
    
    return intRepr(args[0].value) if args[0].value > args[1].value else intRepr(args[1].value)
