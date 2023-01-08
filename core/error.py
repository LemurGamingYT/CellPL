from antlr4.error.ErrorListener import ErrorListener


class ErrorHandler(ErrorListener):
    def __init__(self, lines: list):
        self._lines = lines
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        line = int(line) - 1
        column = int(column)
        
        try:
            print("{}{}^".format(self._lines[line], " " * column))
        except IndexError:
            pass
        
        print("SyntaxError: unexpected content {} at ln {}, col {}".format(offendingSymbol.text, line, column))
        exit(0)


def report_error(name: str, message: str):
    #raise Exception("%sError: %s" % (name, message))
    print("%sError: %s" % (name, message))
    exit(0)
