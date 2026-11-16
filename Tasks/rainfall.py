"""Q1 - Daily rainfall: weekly totals by slicing, max/min, 7-day moving average, dry days."""
import random

random.seed(1)
readings = [random.choice([0, 0, 0, round(random.uniform(0.5, 40), 1)]) for _ in range(365)]


def weekly_totals(r):
    return [round(sum(r[i:i + 7]), 1) for i in range(0, len(r) - len(r) % 7, 7)]


def moving_avg_naive(r, k=7):
    return [sum(r[i:i + k]) / k for i in range(len(r) - k + 1)]   # k additions per window


def moving_avg_running(r, k=7):
    if len(r) < k:
        return []
    s = sum(r[:k]); out = [s / k]
    for i in range(k, len(r)):
        s += r[i] - r[i - k]                                        # 2 operations per window
        out.append(s / k)
    return out


if __name__ == "__main__":
    weeks = weekly_totals(readings)
    print("first 5 weekly totals:", weeks[:5], "| number of full weeks:", len(weeks))
    wet, dry = max(weeks), min(weeks)
    print(f"wettest week {weeks.index(wet) + 1} ({wet} mm), driest week {weeks.index(dry) + 1} ({dry} mm)")
    print(f"max day {readings.index(max(readings)) + 1} ({max(readings)} mm), "
          f"min day {readings.index(min(readings)) + 1} ({min(readings)} mm)")
    ma = moving_avg_running(readings)
    print("7-day moving average, first 3:", [round(x, 2) for x in ma[:3]], "| windows:", len(ma))
    print("same as naive:", all(abs(a - b) < 1e-9 for a, b in zip(ma, moving_avg_naive(readings))))
    dry_days = [d + 1 for d, mm in enumerate(readings) if mm == 0]
    print("dry days:", len(dry_days), "first 10:", dry_days[:10])
    print("readings[7:14] =", readings[7:14], "(week 2)")
    print("readings[-7:]  =", readings[-7:], "(last 7 days)")
    print("readings[:7]   =", readings[:7], "(week 1)")
    print("empty list:", moving_avg_running([]), weekly_totals([]), "| 5 values:", moving_avg_running([1, 2, 3, 4, 5]))
