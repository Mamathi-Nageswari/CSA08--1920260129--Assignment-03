"""Q2 - Memory and speed of tuple vs list; a list inside a tuple; sparse dict grid."""
import sys, timeit

n = 1_000_000
L = list(range(n)); T = tuple(L)
print(f"sys.getsizeof list : {sys.getsizeof(L):,} B | tuple: {sys.getsizeof(T):,} B")
print(f"create list  : {timeit.timeit('[1,2,3,4,5]', number=1_000_000) * 1000:.1f} ns")
print(f"create tuple : {timeit.timeit('(1,2,3,4,5)', number=1_000_000) * 1000:.1f} ns  (constant folded)")
print(f"index list   : {timeit.timeit('L[500000]', globals=globals(), number=1_000_000) * 1000:.1f} ns")
print(f"index tuple  : {timeit.timeit('T[500000]', globals=globals(), number=1_000_000) * 1000:.1f} ns")
stop = ("Guindy", [12, 15])
stop[1].append(20)
print("list inside tuple changed:", stop)
try:
    hash(stop)
except TypeError as e:
    print("hash(stop) ->", e)

R, C = 1000, 1000
dense = [[0] * C for _ in range(R)]
sparse = {}
for r, c in [(5, 7), (500, 2), (999, 999)]:
    dense[r][c] += 3; sparse[(r, c)] = sparse.get((r, c), 0) + 3
dense_bytes = sys.getsizeof(dense) + sum(sys.getsizeof(r) for r in dense)
print(f"1000x1000 grid, 3 busy zones: list of lists {dense_bytes:,} B | dict {sys.getsizeof(sparse)} B")
print("access dense[500][2] =", dense[500][2], "| sparse.get((500, 2), 0) =", sparse.get((500, 2), 0),
      "| empty zone", sparse.get((1, 1), 0))
