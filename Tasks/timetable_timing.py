"""Q6 - Generated timetables of 100, 1,000 and 10,000 trains: scan vs index vs flat list."""
import random, sys, time
from timetable import trains_at, build_index, trains_at_indexed

random.seed(4)
STATIONS = [f"S{i}" for i in range(500)]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def make(n):
    tt = {}
    for no in range(n):
        st = random.sample(STATIONS, 10)
        tt[no] = {"name": f"T{no}", "days": set(random.sample(DAYS, 4)),
                  "stops": [(s, f"{h:02d}:00", f"{h:02d}:05") for h, s in enumerate(st)]}
    return tt


def deep_size(index):
    return sys.getsizeof(index) + sum(sys.getsizeof(v) + sum(sys.getsizeof(x) for x in v) for v in index.values())


print(f"{'trains':>6} | {'scan ms':>8} | {'index ms':>8} | {'flat ms':>8} | {'index memory':>12}")
for n in (100, 1_000, 10_000):
    tt = make(n); idx = build_index(tt)
    flat = [(no, s, a, d, t["days"]) for no, t in tt.items() for s, a, d in t["stops"]]
    q = 50
    s = time.perf_counter(); [trains_at(tt, "S7", "Mon") for _ in range(q)]; ts = time.perf_counter() - s
    s = time.perf_counter(); [trains_at_indexed(tt, idx, "S7", "Mon") for _ in range(q)]; ti = time.perf_counter() - s
    s = time.perf_counter(); [sorted([(no, d) for no, st, a, d, days in flat if st == "S7" and "Mon" in days]) for _ in range(q)]
    tf = time.perf_counter() - s
    print(f"{n:>6} | {ts / q * 1e3:8.3f} | {ti / q * 1e3:8.3f} | {tf / q * 1e3:8.3f} | {deep_size(idx):>10,} B")
