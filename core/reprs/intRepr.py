from .stringRepr import stringRepr
from dataclasses import dataclass
from ..error import report_error
from ..reprs import *


@dataclass(init=True, repr=True, unsafe_hash=True)
class intRepr():
    """Represents an integer"""
    
    value: int
    
    @property
    def hex(self):
        return stringRepr.stringRepr(hex(self.value))
    
    def __add__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value + other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value + other.value)
        else:
            return report_error("Type", "Cannot add type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __sub__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value - other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value - other.value)
        else:
            return report_error("Type", "Cannot subtract type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __mul__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value * other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value * other.value)
        else:
            return report_error("Type", "Cannot multiply type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __truediv__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value / other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value / other.value)
        else:
            return report_error("Type", "Cannot divide type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __mod__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value % other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value % other.value)
        else:
            return report_error("Type", "Cannot mod type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __pow__(self, other):
        if isinstance(other, intRepr):
            return intRepr(self.value ** other.value)
        elif isinstance(other, floatRepr):
            return floatRepr(self.value ** other.value)
        else:
            return report_error("Type", "Cannot pow type 'int' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __eq__(self, other):
        if isinstance(other, intRepr):
            return str(self.value == other.value).lower(), self.value == other.value
        else:
            return "false", False
    
    def __ne__(self, other):
        if isinstance(other, intRepr):
            return str(self.value != other.value).lower(), self.value != other.value
        else:
            return "false", False
    
    def __gt__(self, other):
        if isinstance(other, intRepr):
            return str(self.value > other.value).lower(), self.value > other.value
        else:
            return "false", False
    
    def __lt__(self, other):
        if isinstance(other, intRepr):
            return str(self.value < other.value).lower(), self.value < other.value
        else:
            return "false", False
    
    def __ge__(self, other):
        if isinstance(other, intRepr):
            return str(self.value >= other.value).lower(), self.value >= other.value
        else:
            return "false", False
    
    def __le__(self, other):
        if isinstance(other, intRepr):
            return str(self.value <= other.value).lower(), self.value <= other.value
        else:
            return "false", False

