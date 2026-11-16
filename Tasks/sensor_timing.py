"""Q5 - Time loop / comprehension / map-filter; memory of list vs generator."""
import random, sys, time
from sensors import clean_loop, clean_comp, clean_map

print(f"{'n':>9} | {'loop s':>7} | {'comp s':>7} | {'map s':>7} | {'list B':>10} | {'gen B':>5} | sum list s | sum gen s")
for n in (10_000, 100_000, 1_000_000):
    r = [random.uniform(-60, 60) for _ in range(n)]
    t = [];
    for f in (clean_loop, clean_comp, clean_map):
        s = time.perf_counter(); out = f(r); t.append(time.perf_counter() - s)
    lst = [c for c in r if -50 <= c <= 50]; gen = (c for c in r if -50 <= c <= 50)
    s = time.perf_counter(); sum([c for c in r if -50 <= c <= 50]); sl = time.perf_counter() - s
    s = time.perf_counter(); sum(c for c in r if -50 <= c <= 50); sg = time.perf_counter() - s
    print(f"{n:>9} | {t[0]:7.4f} | {t[1]:7.4f} | {t[2]:7.4f} | {sys.getsizeof(lst):>10,} | "
          f"{sys.getsizeof(gen):>5} | {sl:10.4f} | {sg:9.4f}")
