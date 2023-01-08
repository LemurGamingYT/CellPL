from dataclasses import dataclass


@dataclass(init=True, repr=True, unsafe_hash=True)
class idRepr():
    """Represents a identifier"""
    
    value: str
