# map_output.py - Map output: draws the cities and the tour on a map.
import matplotlib
matplotlib.use("Agg")          # save to file; remove this line to pop up a window
import matplotlib.pyplot as plt


def draw_tour(cities, tour, title, filename):
    """Plot the cities and the closed route, then save it as an image."""
    xs = [cities[i][0] for i in tour] + [cities[tour[0]][0]]   # return to start
    ys = [cities[i][1] for i in tour] + [cities[tour[0]][1]]
    plt.figure(figsize=(7, 7))
    plt.plot(xs, ys, "-", color="indianred", alpha=0.7)
    plt.scatter([c[0] for c in cities], [c[1] for c in cities], color="darkred", zorder=3)
    plt.xlim(0, 220); plt.ylim(0, 220)
    plt.xticks(range(0, 221, 20)); plt.yticks(range(0, 221, 20))
    plt.grid(True, alpha=0.4)
    plt.title(title)
    plt.savefig(filename, dpi=120, bbox_inches="tight")
    plt.close()
