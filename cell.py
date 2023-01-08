"""
cell.py

the cell programming language
"""

from sys import argv

from os import system

from time import perf_counter

try:
    from core.gen.cellLexer import cellLexer
    from core.gen.cellParser import cellParser
    from core.cellVisitor import cellVisitor
except ModuleNotFoundError:
    system("./core/Compile.bat")
    print("Compiled successfully, re-running")
    system("python %s.py" % argv[0])
    exit(0)

from antlr4 import FileStream, CommonTokenStream
from core.error import ErrorHandler

DEBUG = True

def main(f: str) -> None:
    with open(f, "r") as fp:
        lines = fp.readlines()
        if not lines:
            return

    code = FileStream(f)

    lexer = cellLexer(code)
    tokens = CommonTokenStream(lexer)

    parser = cellParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorHandler(lines))
    tree = parser.parse()

    visitor = cellVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    st = perf_counter()

    if len(argv) > 1:
        main(argv[1])
    else:
        main("examples/test.cell")

    if DEBUG:
        time = perf_counter() - st
        print("Time to execute -> %s" % str(time))
