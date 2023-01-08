from ..error import report_error


def lenargs(args: list, needed_args: int, f: str):
    if len(args) > needed_args:
        return report_error("Argument", "'{}' requires {} args, got {}".format(f, needed_args, len(args)))
    elif len(args) < needed_args:
        return report_error("Argument", "'{}' requires {} args, got {}".format(f, needed_args, len(args)))
    
    return True
