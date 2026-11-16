# CSA08 Python Programming - Assignment 3

- Name: ____________________
- Register number: ____________________
- Python version: Python 3.10.12
- Libraries: standard library only (random, time, timeit, sys, copy, collections, tracemalloc). See requirements.txt.

## How to run
Open a terminal in the question folder and run `python3 <file>.py`.

| Folder | Command | Result |
|---|---|---|
| Q1 | `python3 rainfall.py`, `python3 timing.py` | Weekly totals, wettest/driest week, moving average; running sum about 2x faster than naive |
| Q2 | `python3 bus_grid.py`, `python3 tuple_vs_list.py` | Expected output reproduced; shallow vs deep copy; tuple and list memory |
| Q3 | `python3 complaints.py`, `python3 count_timing.py` | Expected output reproduced; Counter fastest, list.count about 20x slower |
| Q4 | `python3 electives.py`, `python3 set_timing.py` | Expected output reproduced; set membership constant time, list linear |
| Q5 | `python3 sensors.py`, `python3 sensor_timing.py` | Three versions identical; generator 104 B vs list 6.7 MB |
| Q6 | `python3 timetable.py`, `python3 timetable_timing.py` | Station queries; index about 70x faster at 10,000 trains |
| Q7 | `python3 contacts.py`, `python3 contacts_timing.py` | 8 lines merged into 4 people; dictionary merge O(n) vs pairwise O(n^2) |

Screenshots of every run are in each folder's `screenshots/` directory.
