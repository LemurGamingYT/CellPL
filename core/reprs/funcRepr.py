from dataclasses import dataclass
from ..gen.cellParser import cellParser
from typing import Callable


@dataclass(init=True, repr=True, unsafe_hash=True)
class funcRepr():
    """Represents a function"""
    
    name: str
    ftype: str
    args: list
    block: cellParser.Stmt_blockContext = None
    python_callable: Callable = None
    public: bool = True
    
    def call(self, visitor, args: list, env):
        if self.block is not None:
            return visitor.visitStmt_block(self.block)
        elif self.python_callable is not None:
            return self.python_callable(args, env)
