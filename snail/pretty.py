from typing import Iterable
from .ast import *

def pretty(node, indent=0):
    pad = "    " * indent

    match node:
        case Program(init, stmts):
            x_range, y_range = init
            init_str = (
                f"{pad}init("
                f"[{x_range.low},{x_range.high}],"
                f"[{y_range.low},{y_range.high}])"
            )
            parts = [init_str]
            parts.extend(pretty(stmt, indent) for stmt in stmts)
            return "\n".join(parts)
        
        case Move(dx, dy):
            return f"{pad}move({dx},{dy})"
        
        case Repeat(body):
            body_str ="\n".join(
                pretty(stmt, indent + 1)
                for stmt in body
            )
            return f"{pad}repeat:\n{body_str}"
        
        case Either(left, right):
            left_str = "\n".join(
                pretty(stmt, indent + 1)
                for stmt in left
            )
            right_str = "\n".join(
                pretty(stmt, indent + 1)
                for stmt in right
            )

            return (
                f"{pad}either:\n"
                f"{left_str}\n"
                f"{pad}or:\n"
                f"{right_str}"
            )

        case _:
            raise TypeError(f"Unknown node: {node!r}")