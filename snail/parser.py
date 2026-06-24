from lark import Lark, Transformer, UnexpectedInput
from lark.indenter import Indenter
from .ast import *
from pathlib import Path

# Postlex action for indentation parsing
class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

# Transformer for Parsetree -> AST transformation
class ASTTransformer(Transformer):
    SIGNED_NUMBER = float
    
    def range(self, items):
        return Range(items[0], items[1])
    
    def init_stmt(self, items):
        return (items[0], items[1])
    
    def move_stmt(self, items):
        return Move(items[0], items[1])

    def repeat_stmt(self, items):
        return Repeat(items[0])
    
    def either_stmt(self, items):
        return Either(items[0], items[1])
    
    def block(self, items):
        return items
    
    def start(self, items):
        init = items[0]
        stmts = items[1:]
        return Program(init, stmts)

grammar_path = Path(__file__).parent / "grammar.lark"

parser = Lark(
    grammar_path.read_text(),
    parser="lalr",
    postlex=TreeIndenter(),
    transformer=ASTTransformer()
)

def parse(source):
    try:
        tree = parser.parse(source)
        return tree
    except UnexpectedInput as e:
        print(f"Syntax error at line {e.line}, column {e.column}")
        print(e.get_context(source))

        # Optional: show what was expected
        if hasattr(e, "expected"):
            expected = ", ".join(sorted(e.expected))
            print(f"Expected one of: {expected}")

        exit(1)