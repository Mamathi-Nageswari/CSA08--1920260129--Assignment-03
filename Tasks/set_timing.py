"""Q4 - x in list vs x in set; nested loops vs & vs sorted two-pointer."""
import time, timeit


def common_nested(a, b):
    return [x for x in a if any(x == y for y in b)]


def common_sorted(a, b):
    a, b = sorted(a), sorted(b); i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i]); i += 1; j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out


print(f"{'n':>9} | {'x in list':>10} | {'x in set':>8}")
for n in (10_000, 100_000, 1_000_000):
    L = [str(192300000 + i) for i in range(n)]; S = set(L); x = L[-1]
    tl = timeit.timeit(lambda: x in L, number=20) / 20; ts = timeit.timeit(lambda: x in S, number=20) / 20
    print(f"{n:>9} | {tl * 1e6:8.1f}us | {ts * 1e9:6.0f}ns")
print(f"{'n each':>7} | {'nested s':>8} | {'sorted s':>8} | {'set & s':>8}")
for n in (1_000, 5_000):
    a = [str(i) for i in range(0, 2 * n, 2)]; b = [str(i) for i in range(0, 3 * n, 3)]
    t = time.perf_counter(); r1 = common_nested(a, b); t1 = time.perf_counter() - t
    t = time.perf_counter(); r2 = common_sorted(a, b); t2 = time.perf_counter() - t
    t = time.perf_counter(); r3 = set(a) & set(b); t3 = time.perf_counter() - t
    assert set(r1) == set(r2) == r3
    print(f"{n:>7} | {t1:8.4f} | {t2:8.4f} | {t3:8.5f}")
