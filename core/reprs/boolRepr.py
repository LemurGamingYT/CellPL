from dataclasses import dataclass


@dataclass(init=True, repr=True, unsafe_hash=True)
class boolRepr():
    """Represents a bool"""
    
    value: str
    rval: bool
