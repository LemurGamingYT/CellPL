from dataclasses import dataclass


@dataclass(init=True, repr=True, unsafe_hash=True)
class nullRepr():
    """Represents null nothing"""
    
    value: None
