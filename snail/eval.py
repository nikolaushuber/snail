from typing import List, Tuple
from .ast import *
import random

State = Tuple[float, float]

def _eval(n : Node, state : List[State], fuel : int = 5):
    match n:
        case Program(init, stmts):
            x_range, y_range = init

            state += [(
                random.uniform(x_range.low, x_range.high),
                random.uniform(y_range.low, y_range.high)
            )]

            for s in stmts:
                _eval(s, state, fuel)

        case Move(dx, dy):
            x, y = state[-1]
            x_ = random.uniform(min(0, dx), max(0, dx))
            y_ = random.uniform(min(0, dy), max(0, dy))

            state += [(x + x_, y + y_)]

        case Repeat(body):
            for s in body:
                _eval(s, state, fuel)

            if fuel > 0:
                _eval(n, state, fuel-1)

        case Either(left, right):
            branch = left if random.choice([True, False]) else right
            
            for s in branch:
                _eval(s, state, fuel)

        case _:
            raise TypeError(f"Unknown node: {n!r}")
        
def eval(p : Program, fuel = 5) -> List[State]:
    state = []
    _eval(p, state, fuel)
    return state