from .baseVisitor import baseVisitor

from ..gen.cellParser import cellParser


class visitArgs(baseVisitor):
    def visit(self, ctx: cellParser.ArgsContext):
        if ctx is not None:
            args = []
            for expr in ctx.expr():
                args.append(self.v.visitExpr(expr))
            
            return args
        else:
            return []
