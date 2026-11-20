# map_input.py - Map input: loads the cities (map coordinates) from a CSV file.
import csv


def load_cities(filename="cities.csv"):
    """Read x,y coordinates from a CSV file and return a list of (x, y) tuples."""
    cities = []
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            cities.append((float(row["x"]), float(row["y"])))
    return cities
