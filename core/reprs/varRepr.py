from dataclasses import dataclass
from typing import Any


@dataclass(init=True, repr=True, unsafe_hash=True)
class varRepr():
    """Represents a variable"""
    
    name: str
    vartype: str
    value: Any
    null_safe: bool = False
    constant: bool = False
    explicit_type: bool = False
