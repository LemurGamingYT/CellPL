from dataclasses import dataclass
from ..error import report_error
from .intRepr import intRepr


@dataclass(init=True, repr=True, unsafe_hash=True)
class floatRepr():
    """Represents a floating point"""
    
    value: float
    
    def __add__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value + other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value + other.value)
        else:
            return report_error("Type", "Cannot add type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __sub__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value - other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value - other.value)
        else:
            return report_error("Type", "Cannot subtract type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __mul__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value * other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value * other.value)
        else:
            return report_error("Type", "Cannot multiply type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __truediv__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value / other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value / other.value)
        else:
            return report_error("Type", "Cannot divide type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __mod__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value % other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value % other.value)
        else:
            return report_error("Type", "Cannot mod type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __pow__(self, other):
        if isinstance(other, floatRepr):
            return floatRepr(self.value ** other.value)
        elif isinstance(other, intRepr):
            return intRepr(self.value ** other.value)
        else:
            return report_error("Type", "Cannot pow type 'float' and type '{}'".format(repr(other).split("Repr")[0]))
    
    def __eq__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value == other.value).lower(), self.value == other.value
        else:
            return "false", False
    
    def __ne__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value != other.value).lower(), self.value != other.value
        else:
            return "false", False
    
    def __gt__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value > other.value).lower(), self.value > other.value
        else:
            return "false", False
    
    def __lt__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value < other.value).lower(), self.value < other.value
        else:
            return "false", False
    
    def __ge__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value >= other.value).lower(), self.value >= other.value
        else:
            return "false", False
    
    def __le__(self, other):
        if isinstance(other, floatRepr):
            return str(self.value <= other.value).lower(), self.value <= other.value
        else:
            return "false", False
