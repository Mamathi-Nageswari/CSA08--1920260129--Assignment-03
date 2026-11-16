"""Q2 - Tuples as keys, zone grid, aliasing and copying (Complete the Code)."""
import copy

rows, cols = 3, 4
bad = [[0] * cols] * rows  # every row is the SAME list object
bad[0][1] = 7

# TODO 1
good = [[0] * cols for _ in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
print(stops[(13.0418, 80.2341)])

try:
    stops[[13.0418, 80.2341]] = "x"
except TypeError as e:
    print("list as key ->", e)

print("ids of bad rows :", [id(r) for r in bad])
print("ids of good rows:", [id(r) for r in good])
for (lat, lon), name in stops.items():
    print(f"  {name:15} lat={lat} lon={lon}")

alias = good; shallow = copy.copy(good); sliced = good[:]; deep = copy.deepcopy(good)
good[1][2] = 5
print("after good[1][2] = 5 ->",
      "alias", alias[1][2], "| copy.copy", shallow[1][2], "| slice", sliced[1][2], "| deepcopy", deep[1][2])
good.append([9] * cols)
print("after good.append   -> len good", len(good), "| shallow", len(shallow), "| deep", len(deep))


def add_passenger(grid, r, c):
    grid[r][c] += 1          # changes the caller's list (same object passed in)


add_passenger(good, 2, 0)
print("caller's grid row 2 after add_passenger:", good[2])
