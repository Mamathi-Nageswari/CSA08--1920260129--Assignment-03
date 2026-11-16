"""Q5 - Cold-storage readings: loop, comprehension, map/filter, alarm minutes."""
import random, sys

random.seed(3)
readings = [round(random.uniform(-1, 11), 1) for _ in range(20)] + [99.0, -60.0]
random.shuffle(readings)


def clean_loop(r):
    c, f = [], []
    for x in r:
        if -50 <= x <= 50:
            c.append(x); f.append(round(x * 9 / 5 + 32, 2))
    return c, f


def clean_comp(r):
    c = [x for x in r if -50 <= x <= 50]                 # [expression for item in iterable if condition]
    return c, [round(x * 9 / 5 + 32, 2) for x in c]


def clean_map(r):
    c = list(filter(lambda x: -50 <= x <= 50, r))
    return c, list(map(lambda x: round(x * 9 / 5 + 32, 2), c))


if __name__ == "__main__":
    print("readings:", readings)
    a, b, c = clean_loop(readings), clean_comp(readings), clean_map(readings)
    print("valid Celsius:", a[0])
    print("Fahrenheit   :", a[1][:8], "...")
    print("three versions identical:", a == b == c)
    alarms = [m for m, x in enumerate(readings) if -50 <= x <= 50 and not 2 <= x <= 8]
    print("alarm minutes (outside 2-8 C):", alarms)
    print("dict comp minute->C:", {m: x for m, x in enumerate(readings) if x > 9})
    print("set comp distinct whole degrees:", {int(x) for x in a[0]})
    print("all valid  :", clean_comp([3.0, 4.5])[0], "| all invalid:", clean_comp([99.0, -70.0])[0])
    gen = (x for x in readings if -50 <= x <= 50)
    print("generator:", gen, "| sum of valid via generator:", round(sum(gen), 1))
