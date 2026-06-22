![](logo/snail_logo_small.png)

# Snail - Programming Language

Snail is a small programming language, designed for an introduction to [Abstract Interpretation](https://en.wikipedia.org/wiki/Abstract_interpretation).

## Installation

In order to install the `snail` tool, run the following command in a terminal:

```bash
git clone https://github.com/nikolaushuber/snail.git
cd snail
uv install tool .
```

Installation instructions for `uv` can be found [here](https://docs.astral.sh/uv/).

## Syntax

Snail only has four commands: `init`, `repeat`, `either/or`, `move`. An example programs looks like this:

```
init([0.0, 1.0], [-1.0, 1.0])
repeat:
    either:
        move(-1.0, 0.0)
    or:
        move(1.0, 1.0)
```

Each program needs to start with an `init`, which places the snail at a random position within the (x, y) range given by the arguments.

The body of a `repeat` block is repeated a random number of times. 

For an `either`/`or` statement, one of the given branches is executed non-deterministically.

A `move` command moves the snail in the direction indicated by the x and y argument. However, these arguments are only limits, and the snail may stop its movement earlier.

## Execution

