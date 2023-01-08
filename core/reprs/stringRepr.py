from dataclasses import dataclass
from ..error import report_error


@dataclass(init=True, repr=True, unsafe_hash=True)
class stringRepr():
    """Represents a string"""
    
    value: str
    
    def lower(self, args: list):
        return stringRepr(self.value.lower())
    
    def upper(self, args: list):
        return stringRepr(self.value.upper())
    
    def capitalize(self, args: list):
        return stringRepr(self.value.capitalize())
    
    def count(self, args: list):
        from .intRepr import intRepr
        
        return intRepr(self.value.count(args[0].value))
    
    def find(self, args: list):
        from .intRepr import intRepr
        
        return intRepr(self.value.index(args[0].value))
    
    @property
    def start(self):
        return stringRepr(self.value[0])
    
    @property
    def end(self):
        return stringRepr(self.value[-1])
    
    @property
    def length(self):
        from .intRepr import intRepr
        
        return intRepr(len(self.value))
    
    def __add__(self, other):
        if isinstance(other, stringRepr):
            return stringRepr(self.value + other.value)
        else:
            return report_error("Cannot add type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __sub__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return stringRepr(self.value - other.value)
        elif isinstance(other, intRepr):
            return stringRepr(self.value[other.value:])
        else:
            return report_error("Cannot subtract type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __mul__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return stringRepr(self.value * other.value)
        elif isinstance(other, intRepr):
            return stringRepr(self.value * other.value)
        else:
            return report_error("Cannot multiply type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __truediv__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return intRepr(len(self.value) / len(other.value))
        else:
            return report_error("Cannot divide type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __mod__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return stringRepr(self.value % other.value)
        elif isinstance(other, intRepr):
            return stringRepr(self.value[other.value:])
        else:
            return report_error("Cannot mod type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __pow__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return stringRepr(self.value ** other.value)
        elif isinstance(other, intRepr):
            return stringRepr(self.value * other.value)
        else:
            return report_error("Cannot pow type 'string' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __eq__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value == other.value).lower(), self.value == other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) == other.value).lower(), len(self.value) == other.value
        else:
            return "false", False
    
    def __ne__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value != other.value).lower(), self.value != other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) != other.value).lower(), len(self.value) != other.value
        else:
            return "false", False
    
    def __gt__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value > other.value).lower(), self.value > other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) > other.value).lower(), len(self.value) > other.value
        else:
            return "false", False
    
    def __lt__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value < other.value).lower(), self.value < other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) < other.value).lower(), len(self.value) < other.value
        else:
            return "false", False
    
    def __ge__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value >= other.value).lower(), self.value >= other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) >= other.value).lower(), len(self.value) >= other.value
        else:
            return "false", False
    
    def __le__(self, other):
        from .intRepr import intRepr
        
        if isinstance(other, stringRepr):
            return str(self.value <= other.value).lower(), self.value <= other.value
        elif isinstance(other, intRepr):
            return str(len(self.value) <= other.value).lower(), len(self.value) <= other.value
        else:
            return "false", False

