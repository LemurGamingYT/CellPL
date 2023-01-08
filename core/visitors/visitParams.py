from .baseVisitor import baseVisitor

from ..gen.cellParser import cellParser

from ..other.constants import ALL_TYPE_KWS


class visitParams(baseVisitor):
    def visit(self, ctx: cellParser.ParamsContext):
        if ctx is not None:
            args = []
            skip = []
            for i, param in enumerate(ctx.ID()):
                if i in skip: continue
                
                param = str(param)
                
                if param in ALL_TYPE_KWS:
                    args.append([param, str(ctx.ID(i + 1))])
                    skip.append(i + 1)
                else:
                    args.append(["any", param])
            
            return args
        else:
            return []
