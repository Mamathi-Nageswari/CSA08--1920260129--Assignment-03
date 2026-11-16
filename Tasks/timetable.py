"""Q6 - Railway timetable as nested data; station query; index."""
timetable = {
    12635: {"name": "Vaigai Express", "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
            "stops": [("Chennai Egmore", None, "13:40"), ("Tambaram", "14:08", "14:10"),
                      ("Villupuram", "15:45", "15:50"), ("Tiruchchirappalli", "18:25", "18:30"),
                      ("Madurai", "21:15", None)]},
    12605: {"name": "Pallavan Express", "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
            "stops": [("Chennai Egmore", None, "15:45"), ("Tambaram", "16:13", "16:15"),
                      ("Villupuram", "17:45", "17:50"), ("Karaikudi", "22:45", None)]},
    16127: {"name": "Guruvayur Express", "days": {"Mon", "Wed", "Fri", "Sun"},
            "stops": [("Chennai Egmore", None, "10:20"), ("Tambaram", "10:48", "10:50"),
                      ("Villupuram", "12:25", "12:30"), ("Madurai", "18:00", "18:05"), ("Guruvayur", "05:10", None)]},
    20605: {"name": "Tiruchendur Express", "days": {"Tue", "Thu", "Sat"},
            "stops": [("Chennai Egmore", None, "16:05"), ("Villupuram", "18:00", "18:05"),
                      ("Madurai", "23:05", "23:10"), ("Tiruchendur", "04:40", None)]},
    12693: {"name": "Pearl City Express", "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
            "stops": [("Chennai Egmore", None, "19:15"), ("Tambaram", "19:43", "19:45"),
                      ("Villupuram", "21:20", "21:25"), ("Madurai", "02:40", "02:45"), ("Tuticorin", "06:10", None)]},
}


def trains_at(tt, station, day):
    """Scan every train and every stop: O(total stops)."""
    found = []
    for no, t in tt.items():
        if day in t["days"]:
            for st, arr, dep in t["stops"]:
                if st == station and dep:
                    found.append((no, t["name"], dep))
    return sorted(found, key=lambda x: x[2])


def build_index(tt):
    index = {}
    for no, t in tt.items():
        for st, arr, dep in t["stops"]:
            index.setdefault(st, []).append((no, dep))
    return index


def trains_at_indexed(tt, index, station, day):
    """Look only at the trains that stop there: O(trains at the station)."""
    return sorted(((no, tt[no]["name"], dep) for no, dep in index.get(station, [])
                   if dep and day in tt[no]["days"]), key=lambda x: x[2])


if __name__ == "__main__":
    print("departure time of the 3rd station of 12635:", timetable[12635]["stops"][2][2])
    for station, day in [("Villupuram", "Tue"), ("Villupuram", "Mon"), ("Kanyakumari", "Mon"), ("Tiruchendur", "Mon")]:
        print(f"\n{station} on {day}:")
        rows = trains_at(timetable, station, day)
        assert rows == trains_at_indexed(timetable, build_index(timetable), station, day)
        if not rows:
            print("  no trains")
        for no, name, dep in rows:
            print(f"  {no:<6} {name:<22} dep {dep}")
