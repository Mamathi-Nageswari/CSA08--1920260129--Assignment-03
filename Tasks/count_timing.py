"""Q3 - dict.get vs list.count vs collections.Counter for 1,000 to 100,000 complaints."""
import random, time
from collections import Counter
from complaints import frequencies

random.seed(2)
VOCAB = [f"word{i}" for i in range(300)] + ["not", "high"]
STOP = {"not", "high"}


def by_list_count(texts, stop):
    words = [w for t in texts for w in t.split() if w not in stop]
    return {w: words.count(w) for w in set(words)}   # one full scan per distinct word


def by_counter(texts, stop):
    return Counter(w for t in texts for w in t.split() if w not in stop)


print(f"{'complaints':>10} | {'dict.get s':>10} | {'list.count s':>12} | {'Counter s':>9}")
for n in (1_000, 10_000, 100_000):
    texts = [" ".join(random.choices(VOCAB, k=6)) for _ in range(n)]
    res = []
    for f in (frequencies, by_list_count, by_counter):
        t = time.perf_counter(); r = f(texts, STOP); res.append((time.perf_counter() - t, dict(r)))
    assert res[0][1] == res[1][1] == res[2][1]
    print(f"{n:>10} | {res[0][0]:10.4f} | {res[1][0]:12.4f} | {res[2][0]:9.4f}")
