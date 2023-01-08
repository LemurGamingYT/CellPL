"""
cureVisitor.py

an overridden version of the cureVisitor
"""

# import the cellVisitor module
from .gen.cellVisitor import cellVisitor

# import the os module to get the current working directory & list directory
from os import getcwd, listdir

# import the glob module to get all the python files in a directory
from glob import glob

from .error import report_error

from threading import Thread

# import the environment
from .env import Environment

# import the reprs
from .reprs import *

from .other.constants import ALL_TYPE_KWS

# import the cellParser
from .gen.cellParser import cellParser


# override the cellVisitor
class cellVisitor(cellVisitor):
    def __init__(self) -> None:
        self.env = Environment()
        
        self.tasks = {}
        
        for visitor in listdir("%s/core/visitors" % getcwd()):
            if visitor == "baseVisitor.py" or visitor == "__pycache__": continue
            
            exec("""from {cwd}.visitors.{v} import {v}
setattr(self, '{v}', {v}(self).visit)""".format(cwd="core", v=visitor[:-3]))
    
    ###########################################################################
    ################## STATEMENTS
    ###########################################################################
    
    def visitIf_stmt(self, ctx: cellParser.If_stmtContext):
        c = self.visitConditional_block(ctx.conditional_block()[0])
        
        if c.rval:
            return self.visitStmt_block(ctx.stmt_block()[0])
        elif not c.rval:
            if len(ctx.IF()) > 1:
                for i in ctx.IF()[1:]:
                    c = self.visitConditional_block(ctx.conditional_block(i))
                    if c.rval:
                        return self.visitStmt_block(ctx.stmt_block()[i])
                    elif not c.rval:
                        continue
            elif len(ctx.ELSE()) == 1 and len(ctx.IF()) == 1:
                return self.visitStmt_block(ctx.stmt_block()[-1])
    
    def visitWhile_stmt(self, ctx: cellParser.While_stmtContext):
        c = self.visitConditional_block(ctx.conditional_block())
        
        while c.rval:
            self.visitStmt_block(ctx.stmt_block())
            
            c = self.visitConditional_block(ctx.conditional_block())
    
    def visitFor_stmt(self, ctx: cellParser.For_stmtContext):
        counter = str(ctx.ID(0))
        
        self.env.add_var(varRepr(counter, "int", intRepr(0), constant=True))
        
        c = self.visitConditional_block(ctx.conditional_block())
        
        while c.rval:
            self.visitStmt_block(ctx.stmt_block())
            
            cval = self.env.get_var(counter).value.value
            if ctx.INCR() is not None:
                self.env.set_var(counter, varRepr(counter, "int", intRepr(cval + 1), constant=True))
            elif ctx.DECR() is not None:
                self.env.set_var(counter, varRepr(counter, "int", intRepr(cval - 1), constant=True))
            
            c = self.visitConditional_block(ctx.conditional_block())
    
    ###########################################################################
    ################## ASSIGNMENTS
    ###########################################################################
    
    def visitVarassignment(self, ctx: cellParser.VarassignmentContext):
        name = str(ctx.ID(0))
        expl_type = False
        et = None
        if name in ALL_TYPE_KWS:
            expl_type = True
            et = name
            name = str(ctx.ID(1))
        
        value = self.visitExpr(ctx.expr())
        
        type = repr(value).split("Repr")[0]
        if et is None:
            et = type
        
        null_safe = True if ctx.QUESTION() is not None else False
        
        if name in self.env.variables:
            old = self.env.get_var(name)
            r = varRepr(name, type, value, null_safe, name.isupper(), expl_type)
            
            if name.isupper():
                return report_error("Type", "Constant variable '%s' cannot be changed" % name)
            
            self.env.set_var(name, varRepr(name, type, value, null_safe, name.isupper(), expl_type))
            
            try:
                et
            except UnboundLocalError:
                return None
            
            if r.vartype != et and old.explicit_type:
                return report_error("Type", "variable '{}' does not match it's explicit type".format(name))
            
            return None
        
        if ctx.atype.text in ("+=", "-=", "*=", "/=", "%=", "**="):
            atype = ctx.atype.text[:-1]
            r = self.env.get_var(name)
            
            if atype == "+":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value + value, r.null_safe, r.constant, r.explicit_type))
            elif atype == "-":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value - value, r.null_safe, r.constant, r.explicit_type))
            elif atype == "*":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value * value, r.null_safe, r.constant, r.explicit_type))
            elif atype == "/":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value / value, r.null_safe, r.constant, r.explicit_type))
            elif atype == "%":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value % value, r.null_safe, r.constant, r.explicit_type))
            elif atype == "**":
                self.env.set_var(r.name, varRepr(r.name, r.vartype, r.value ** value, r.null_safe, r.constant, r.explicit_type))
        
            return None
        else:
            r = varRepr(name, type, value, null_safe, name.isupper(), expl_type)
            
            if r.vartype != et:
                return report_error("Type", "variable '{}' does not match it's explicit type".format(name))
            
            self.env.add_var(r)
            
            return None
    
    def visitFuncassignment(self, ctx: cellParser.FuncassignmentContext):
        public = True
        if ctx.PUBLIC() is not None or ctx.PRIVATE() is not None:
            public = True if ctx.PUBLIC() is not None else False
            if not public and ctx.PRIVATE() is not None:
                public = False
        
        name = str(ctx.ID(0))
        ftype = ""
        if name in ALL_TYPE_KWS:
            ftype = name
            name = str(ctx.ID(1))
        
        block = ctx.stmt_block()
        
        args = self.visitParams(ctx.params())
        
        r = funcRepr(name, ftype, args, block, public=public)
        self.env.add_func(r)
    
    ###########################################################################
    ################## FUNCTIONS
    ###########################################################################
    
    def visitCall(self, ctx: cellParser.CallContext):
        fname = str(ctx.ID())
        args = self.visitArgs(ctx.args())
        
        if fname in self.env.functions:
            reprfunc = self.env.get_func(fname)
            
            for val, name in zip(args, reprfunc.args):
                r = varRepr(name[1], name[0], val, True)
                self.env.add_var(r)
            
            return reprfunc.call(self, args, self.env)
        
        for func in glob("core/other/funcs/*.py"):
            func = func.split("\\")[1][:-3]
            if fname == func:
                exec("""import core.other.funcs.{f} as {f}
args = {args}
for i, arg in enumerate(args):
    if isinstance(arg, idRepr):
        args[i] = self.env.get_var(arg.value).value

out = {f}._{f}(args, self.env)""".format(f=func, args=args))
                return locals()["out"]
    
    ###########################################################################
    ################## OTHER
    ###########################################################################
    
    def visitGetattribs(self, ctx: cellParser.GetattribsContext):
        if ctx.STRING() is not None:
            obj = stringRepr(str(ctx.STRING())[1:-1])
            
            attr = str(ctx.ID(0))
        else:
            obj = str(ctx.ID(0))
        
            attr = str(ctx.ID(1))
            
            for name in glob("core/other/classes/*.py"):
                name = name.split("\\")[-1][:-3]
                
                if name == obj:
                    exec("""from core.other.classes.{name} import {name}
args = {args}
for i, arg in enumerate(args):
    if isinstance(arg, idRepr):
        args[i] = self.env.get_var(arg.value).value

out = getattr({name}, '{a}')(args, self.env)""".format(name=name, a=attr, args=self.visitArgs(ctx.args())))
                    return locals()["out"]
            
            obj = self.env.get_var(obj).value
        
        try: 
            func = getattr(obj, attr)
        except AttributeError:
            return report_error("Attribute", "type '{}' has no attribute '{}'".format(repr(obj).split("Repr")[0], attr))
        
        if str(type(func)) == "<class 'method'>":
            args = self.visitArgs(ctx.args())
            
            return getattr(obj, attr)(args)
        else:
            return getattr(obj, attr)
    
    def visitTask_usage(self, ctx: cellParser.Task_usageContext):
        if ctx.NEW() is not None:
            args = self.visitArgs(ctx.args())
            func = args[0].value
            
            frepr = self.env.get_func(func)
            
            t = Thread(target=self.visitStmt_block(frepr.block))
            t.daemon = True
            self.tasks[func] = [frepr, t]
        elif ctx.TASK_RESUME() is not None:
            args = self.visitArgs(ctx.args())
            func = args[0].value
            
            t = self.tasks.get(func)
            if t is None:
                return report_error("Concurrent", "Untasked function being called")
            
            t[1].start()
    
    def visitType_conversion(self, ctx: cellParser.Type_conversionContext):
        t = str(ctx.ID(0))
        
        expr = ""
        for attr in dir(ctx):
            if attr in ("ID", "STRING", "INT", "FLOAT", "BOOL"):
                if getattr(ctx, attr)() is not None:
                    value = str(getattr(ctx, attr)())
                    
                    if attr == "STRING":
                        expr = stringRepr(str(value)[1:-1])
                    elif attr == "INT":
                        expr = intRepr(int(value))
                    elif attr == "FLOAT":
                        expr = floatRepr(float(value))
                    elif attr == "BOOL":
                        expr = boolRepr(str(value), True if value == "true" else False)
                    elif attr == "NULL":
                        expr = nullRepr(None)
                    elif attr == "ID":
                        expr = idRepr(str(value))
        
        if t in ALL_TYPE_KWS:
            if t == "int":
                try:
                    return intRepr(int(expr.value))
                except TypeError:
                    return report_error("Type", "Cannot convert {} to {}".format(expr.value, t))
            elif t == "float":
                try:
                    return floatRepr(float(expr.value))
                except TypeError:
                    return report_error("Type", "Cannot convert {} to {}".format(expr.value, t))
            elif t == "string":
                try:
                    return stringRepr(str(expr.value))
                except TypeError:
                    return report_error("Type", "Cannot convert {} to {}".format(expr.value, t))
            elif t == "bool":
                try:
                    if expr.value == 0:
                        return boolRepr("false", False)
                    elif expr.value == 1:
                        return boolRepr("true", True)
                    else:
                        return report_error("Type", "Cannot convert {} to {}".format(expr.value, t))
                except TypeError:
                    return report_error("Type", "Cannot convert {} to {}".format(expr.value, t))
        # else:
        #     return report_error("Type", "{} is not a valid type".format(t))
        
    def visitArray(self, ctx: cellParser.ArrayContext):
        return arrayRepr(self.visitArgs(ctx.args()))
    
    ###########################################################################
    ################## EXPRESSION
    ###########################################################################
    
    def visitExpr(self, ctx: cellParser.ExprContext):
        if ctx.getattribs() is not None:
            return self.visitGetattribs(ctx.getattribs())
        elif ctx.call() is not None:
            return self.visitCall(ctx.call())
        elif ctx.type_conversion() is not None:
            return self.visitType_conversion(ctx.type_conversion())
        elif ctx.mem_addr() is not None:
            return self.visitMem_addr(ctx.mem_addr())
        elif ctx.task_usage() is not None:
            return self.visitTask_usage(ctx.task_usage())
        elif ctx.array() is not None:
            return self.visitArray(ctx.array())
        elif not ctx.expr():
            for attr in dir(ctx):
                if attr in ("ID", "STRING", "INT", "FLOAT", "BOOL", "NULL"):
                    if getattr(ctx, attr)() is not None:
                        value = str(getattr(ctx, attr)())
                        
                        if attr == "STRING":
                            return stringRepr(str(value)[1:-1])
                        elif attr == "INT":
                            return intRepr(int(value))
                        elif attr == "FLOAT":
                            return floatRepr(float(value))
                        elif attr == "BOOL":
                            return boolRepr(str(value), True if value == "true" else False)
                        elif attr == "NULL":
                            return nullRepr(None)
                        elif attr == "ID":
                            return idRepr(str(value))
        elif ctx.expr() != []:
            op = ctx.op.text
            
            val1 = self.visitExpr(ctx.expr(0))
            val2 = self.visitExpr(ctx.expr(1))
            
            if isinstance(val1, idRepr):
                val1 = self.env.get_var(val1.value).value
            
            if isinstance(val2, idRepr):
                val2 = self.env.get_var(val2.value).value
            
            try:
                out = eval("{}{}{}".format(val1, op, val2))
            except TypeError:
                return report_error("Type", "Cannot operate on type '{}' and type '{}'".format(repr(val1).split("Repr")[0], repr(val2).split("Repr")[0]))
            
            if isinstance(out, tuple):
                out = boolRepr(out[0], out[1])
            
            return out
