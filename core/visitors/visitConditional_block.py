from .baseVisitor import baseVisitor

from ..gen.cellParser import cellParser

from ..reprs import *


class visitConditional_block(baseVisitor):
    def visit(self, ctx: cellParser.Conditional_blockContext):
        expr = self.v.visitExpr(ctx.expr())
        
        return expr
