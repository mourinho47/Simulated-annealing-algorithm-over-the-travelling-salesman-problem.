# sa_tutorial.py - Simulated Annealing for the Travelling Salesman Problem.
# Based on: theprojectspot.com "Simulated Annealing for beginners" (Java, ported to Python).
# Usage: python sa_tutorial.py [start_temp] [cooling_rate]
import math
import random
import sys

from map_input import load_cities
from map_output import draw_tour


def distance(a, b):
    """Euclidean distance between two cities."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def tour_distance(cities, tour):
    """Total length of the closed tour (returns to the starting city)."""
    return sum(distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
               for i in range(len(tour)))


def acceptance_probability(current, new, temperature):
    """Always accept a better tour; accept a worse one with probability exp(-dE/T)."""
    if new < current:
        return 1.0
    return math.exp((current - new) / temperature)


def anneal(cities, temp=10000.0, cooling_rate=0.003, seed=None):
    """Run simulated annealing. Returns (initial_tour, best_tour)."""
    if seed is not None:
        random.seed(seed)
    n = len(cities)
    current = list(range(n))
    random.shuffle(current)                    # random starting tour
    initial = current[:]
    best = current[:]
    current_len = best_len = tour_distance(cities, current)

    while temp > 1:
        new = current[:]
        i, j = random.sample(range(n), 2)      # neighbour move: swap two cities
        new[i], new[j] = new[j], new[i]
        new_len = tour_distance(cities, new)

        if acceptance_probability(current_len, new_len, temp) > random.random():
            current, current_len = new, new_len
        if current_len < best_len:
            best, best_len = current[:], current_len

        temp *= 1 - cooling_rate               # cool down
    return initial, best


if __name__ == "__main__":
    start_temp = float(sys.argv[1]) if len(sys.argv) > 1 else 10000.0
    cooling = float(sys.argv[2]) if len(sys.argv) > 2 else 0.003

    cities = load_cities("cities.csv")
    print(f"Loaded {len(cities)} cities")
    print(f"Starting temperature = {start_temp}, cooling rate = {cooling}")

    initial, best = anneal(cities, start_temp, cooling)
    d0, d1 = tour_distance(cities, initial), tour_distance(cities, best)
    print(f"Initial distance: {d0:.2f}")
    print(f"Final distance:   {d1:.2f}")
    print("Final tour:", best)

    draw_tour(cities, initial, f"Initial route ({d0:.1f})", "initial_route.png")
    draw_tour(cities, best, f"Final route ({d1:.1f})", "final_route.png")
    print("Saved initial_route.png and final_route.png")
