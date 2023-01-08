from .baseVisitor import baseVisitor

from ..reprs import *

from ..gen.cellParser import cellParser


class visitMem_addr(baseVisitor):
    def visit(self, ctx: cellParser.Mem_addrContext):
        return stringRepr(hex(id(self.v.env.get_var(str(ctx.ID())))))
