import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Tuple
import random

flower_colors = [
    "#ff4d6d", "#ff006e", "#fb5607",
    "#ff7f11", "#ffb703", "#ffd166",
    "#ffe66d", "#fff3b0", "#ffafcc",
    "#ffc8dd", "#ff8fab", "#f78fb3",
    "#9b5de5", "#b5179e", "#c77dff",
    "#7209b7", "#4cc9f0", "#4895ef",
    "#4361ee", "#80ed99", "#57cc99",
    "#38a3a5", "#fffaf0", "#f8f9fa",
    "#e9ecef"
]

Trace = List[Tuple[float, float]]
Garden = Tuple[float, float, float, float]

def plot(traces : List[Trace], gardens : List[Garden], flowers : bool, filename : str, out):
    fig, ax = plt.subplots()

    for trace in traces:
        x, y = zip(*trace)
        line, = plt.plot(x, y, linewidth=2)

        # last point
        x_last, y_last = trace[-1]

        plt.scatter(
            x_last,
            y_last,
            s=120,              # size of dot
            color=line.get_color(),
            zorder=3            # ensures it sits on top
        )

    for (x, y, dx, dy) in gardens:
        rect = patches.Rectangle(
            (x, y), dx, dy,
            linewidth=3,
            edgecolor="#457328",
            facecolor="#7ec850"
        )
        ax.add_patch(rect)

        if flowers:
            area = dx * dy
            density = 1.5
            num_flowers = int(area * density)

            for _ in range(num_flowers):
                flower_x = random.uniform(x, x + dx)
                flower_y = random.uniform(y, y + dy)

                r = random.uniform(0.05, 0.25)
                flower = patches.Circle(
                    (flower_x, flower_y), 
                    r,
                    color=random.choice(flower_colors), 
                    alpha=0.45,
                    hatch='OO',
                    linestyle=':'
                )
                ax.add_patch(flower)

    ax.set_aspect('equal', adjustable='box')
    ax.set_axisbelow(True)
    ax.grid(True)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    # Enforce minimum extent
    plt.xlim(min(xmin, 0), max(xmax, 5))
    plt.ylim(min(ymin, 0), max(ymax, 5))

    fig.canvas.manager.set_window_title(filename)

    if out is not None:
        plt.savefig(out)
    else:
        plt.show()