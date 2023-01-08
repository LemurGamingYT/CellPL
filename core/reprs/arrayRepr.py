from dataclasses import dataclass
from ..error import report_error
from typing import List, Any
from .intRepr import intRepr
from .nullRepr import nullRepr


@dataclass(init=True, repr=True, unsafe_hash=True)
class arrayRepr():
    """Represents an array"""
    
    value: List[Any]
    
    def add(self, args: list):
        self.value.append(args[0])
        return None
    
    def rem(self, args: list):
        try:
            self.value.pop(args[0].value)
        except IndexError:
            return report_error("Index", "Index out of range")
        
        return None
    
    def remove(self, args: list):
        try:
            self.value.pop(args[0].value)
        except IndexError:
            return report_error("Index", "Index out of range")
        
        return None
    
    def remove_duplicates(self, args: list):
        rnew = []
        new = []
        for item in self.value:
            if str(item.value) not in new:
                new.append(str(item.value))
                rnew.append(item)
        
        return arrayRepr(rnew)
    
    def reverse(self, args: list):
        self.value.reverse()
        
        return nullRepr(self.value)
    
    def bubblesort(self, args: list):
        for _ in range(len(self.value)):
            for j in range(len(self.value) - 1):
                if self.value[j] > self.value[j + 1]:
                    self.value[j], self.value[j + 1] = self.value[j + 1], self.value[j]
    
    def tsort(self, args: list):
        self.value.sort()
        
        return nullRepr(None)
    
    @property
    def first(self):
        try:
            return self.value[0]
        except IndexError:
            return report_error("Index", "Length of array is 0")
    
    @property
    def last(self):
        try:
            return self.value[-1]
        except IndexError:
            return report_error("Index", "Length of array is 0")
    
    @property
    def length(self):
        return intRepr(len(self.value))
    
    def __add__(self, other):
        self.add([other])
        return arrayRepr(self.value)
        
    def __sub__(self, other):
        self.rem([other])
        return arrayRepr(self.value)
    
    def __mul__(self, other):
        if isinstance(other, intRepr):
            val = self.value
            for v in self.value:
                val.append(v)
            
            return arrayRepr(val)
        else:
            return report_error("Cannot multiply type 'list' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __truediv__(self, other):
        if isinstance(other, intRepr):
            val = self.value
            for i, _ in enumerate(range(other.value)):
                try:
                    val.pop(i)
                except IndexError:
                    return report_error("Index", "Index out of range")
            
            return arrayRepr(val)
        else:
            return report_error("Cannot divide type 'list' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __mod__(self, other):
        if isinstance(other, intRepr):
            val = self.value
            for i, _ in enumerate(range(other.value)):
                try:
                    val.pop(i)
                except IndexError:
                    return report_error("Index", "Index out of range")
            
            return arrayRepr(val)
        elif isinstance(other, arrayRepr):
            val = self.value
            for i, _ in enumerate(len(other.value)):
                try:
                    val.pop(i)
                except IndexError:
                    return report_error("Index", "Index out of range")
            
            return arrayRepr(val)
        else:
            return report_error("Cannot mod type 'list' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __pow__(self, other):
        if isinstance(other, intRepr):
            val = self.value
            for v in self.value:
                val.append(v)
            
            return arrayRepr(val)
        else:
            return report_error("Cannot pow type 'list' to '{}'".format(repr(other).split("Repr")[0]))
    
    def __eq__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value == other.value), self.value == other.value
        else:
            return "false", False
    
    def __ne__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value != other.value), self.value != other.value
        else:
            return "false", False
    
    def __gt__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value > other.value), self.value > other.value
        else:
            return "false", False
    
    def __lt__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value < other.value), self.value < other.value
        else:
            return "false", False
    
    def __ge__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value >= other.value), self.value >= other.value
        else:
            return "false", False
    
    def __le__(self, other):
        if isinstance(other, arrayRepr):
            return str(self.value <= other.value), self.value <= other.value
        else:
            return "false", False
