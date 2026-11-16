"""Q7 - Dictionary merge vs comparing every pair, for 1,000 and 100,000 contacts."""
import random, time, tracemalloc
from contacts import merge, norm_number

random.seed(5)


def make(n):
    rows = []
    for i in range(n):
        num = str(9000000000 + random.randrange(n // 2))   # about half are duplicates
        fmt = random.choice([num, "+91 " + num[:5] + " " + num[5:], "0" + num])
        rows.append(f"Person {num[-4:]}, {fmt}")
    return {"all": rows}


def merge_pairs(rows):
    nums = [norm_number(r.split(",")[1]) for r in rows]
    group = list(range(len(rows))); comparisons = 0
    for i in range(len(rows)):
        for j in range(i):
            comparisons += 1
            if nums[i] == nums[j]:
                group[i] = group[j]; break
    return len(set(group)), comparisons


print(f"{'contacts':>8} | {'dict s':>7} | {'dict peak MB':>12} | {'people':>6} | {'pairs s':>8} | {'comparisons':>12}")
for n in (1_000, 10_000, 100_000):
    src = make(n)
    tracemalloc.start(); t = time.perf_counter(); people, _ = merge(src); td = time.perf_counter() - t
    peak = tracemalloc.get_traced_memory()[1] / 1e6; tracemalloc.stop()
    if n <= 10_000:
        t = time.perf_counter(); groups, comp = merge_pairs(src["all"]); tp = time.perf_counter() - t
        assert groups == len(people)
        pair = f"{tp:8.3f} | {comp:>12,}"
    else:
        pair = f"{'~' + str(round(tp * 100)) + ' (est)':>8} | {'~' + format(n * n // 4, ','):>12}"
    print(f"{n:>8} | {td:7.3f} | {peak:12.2f} | {len(people):>6} | {pair}")
