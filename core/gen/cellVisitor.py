# Generated from cell.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cellParser import cellParser
else:
    from cellParser import cellParser

# This class defines a complete generic visitor for a parse tree produced by cellParser.

class cellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cellParser#parse.
    def visitParse(self, ctx:cellParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#stmts.
    def visitStmts(self, ctx:cellParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#stmt.
    def visitStmt(self, ctx:cellParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#if_stmt.
    def visitIf_stmt(self, ctx:cellParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#while_stmt.
    def visitWhile_stmt(self, ctx:cellParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#for_stmt.
    def visitFor_stmt(self, ctx:cellParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#varassignment.
    def visitVarassignment(self, ctx:cellParser.VarassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#funcassignment.
    def visitFuncassignment(self, ctx:cellParser.FuncassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#conditional_block.
    def visitConditional_block(self, ctx:cellParser.Conditional_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#stmt_block.
    def visitStmt_block(self, ctx:cellParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#call.
    def visitCall(self, ctx:cellParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#args.
    def visitArgs(self, ctx:cellParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#params.
    def visitParams(self, ctx:cellParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#type_conversion.
    def visitType_conversion(self, ctx:cellParser.Type_conversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#mem_addr.
    def visitMem_addr(self, ctx:cellParser.Mem_addrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#getattribs.
    def visitGetattribs(self, ctx:cellParser.GetattribsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#task_usage.
    def visitTask_usage(self, ctx:cellParser.Task_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#array.
    def visitArray(self, ctx:cellParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cellParser#expr.
    def visitExpr(self, ctx:cellParser.ExprContext):
        return self.visitChildren(ctx)



del cellParser