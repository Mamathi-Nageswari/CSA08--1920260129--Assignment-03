"""Q1 - Naive vs running-sum moving average for 365, 36,500 and 365,000 readings."""
import random, time
from collections import deque
from rainfall import moving_avg_naive, moving_avg_running


def moving_avg_deque(r, k=7):
    window, s, out = deque(maxlen=k), 0, []
    for x in r:
        if len(window) == k:
            s -= window[0]
        window.append(x); s += x
        if len(window) == k:
            out.append(s / k)
    return out


print(f"{'n':>7} | {'naive adds':>10} | {'running adds':>12} | {'naive s':>8} | {'running s':>9} | {'deque s':>8}")
for n in (365, 36_500, 365_000):
    r = [random.uniform(0, 40) for _ in range(n)]
    t = time.perf_counter(); a = moving_avg_naive(r); tn = time.perf_counter() - t
    t = time.perf_counter(); b = moving_avg_running(r); tr = time.perf_counter() - t
    t = time.perf_counter(); c = moving_avg_deque(r); td = time.perf_counter() - t
    assert len(a) == len(b) == len(c)
    print(f"{n:>7} | {6 * (n - 6):>10} | {6 + 2 * (n - 7):>12} | {tn:8.4f} | {tr:9.4f} | {td:8.4f}")
