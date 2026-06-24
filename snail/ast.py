from dataclasses import dataclass
from typing import List, Union, Tuple

# AST base class
class Node:
    pass

@dataclass
class Program(Node):
    init: Tuple[Range, Range]
    stmts: List[Statement]

@dataclass
class Range(Node):
    low: float
    high: float

@dataclass
class Move(Node):
    dx: float
    dy: float

@dataclass
class Repeat(Node):
    body: List[Statement]

@dataclass
class Either(Node):
    left: List[Statement]
    right: List[Statement]

Statement = Union[Move, Repeat, Either]

