import argparse
from pathlib import Path

from .parser import parser
from .eval import eval
from .pretty import pretty
from .plot import plot

def main():
    cli = argparse.ArgumentParser()

    cli.add_argument("file")
    cli.add_argument("--dump", action="store_true")
    cli.add_argument("--eval", action="store_true")
    cli.add_argument("--runs", type=int, default=1)
    cli.add_argument("--garden", default=None)
    cli.add_argument("--out", default=None)

    args = cli.parse_args()

    source = Path(args.file).read_text()

    ast = parser.parse(source)

    # parse gardens
    gardens = []
    if args.garden is not None:
        with open(args.garden, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                gardens.append(tuple(map(float, parts)))


    if args.dump:
        print(pretty(ast))
    elif args.eval:
        trace = eval(ast)
        
        for x, y in trace:
            print(f"({x:+.2f}, {y:+.2f})")
    else:
        traces = [eval(ast) for _ in range(0, args.runs)]
        plot(traces, gardens, args.out)


if __name__ == '__main__':
    main()