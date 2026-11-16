"""Q7 - Merge contacts from two phones and a SIM, keyed by normalised number."""
TITLES = {"dr", "mr", "mrs", "ms", "prof"}


def norm_number(raw):
    """'+91 98400 12345', '098400-12345', '9840012345' -> '9840012345' (last 10 digits)."""
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits[-10:] if len(digits) >= 10 else None


def norm_name(raw):
    """'Dr. Ravi' / 'ravi kumar ' -> 'ravi' / 'ravi kumar' (lower case, no titles or dots)."""
    words = [w.strip(".").lower() for w in raw.replace(".", ". ").split()]
    return " ".join(w for w in words if w and w not in TITLES)


def valid_email(e):
    e = e.strip().lower()
    return e if e.count("@") == 1 and "." in e.split("@")[1] and " " not in e else None


def merge(sources):
    people = {}                 # normalised number -> person record
    owner = {}                  # every number -> key of its person
    log = []
    for src, rows in sources.items():
        for line_no, row in enumerate(rows, 1):
            parts = [p.strip() for p in row.split(",")]
            if len(parts) < 2 or not parts[0]:
                log.append(f"{src}:{line_no} damaged: {row!r}"); continue
            name, numbers = norm_name(parts[0]), {n for n in map(norm_number, parts[1].split(";")) if n}
            emails = {e for e in map(valid_email, parts[2].split(";")) if e} if len(parts) > 2 else set()
            if not numbers and not emails:
                log.append(f"{src}:{line_no} no number or e-mail: {row!r}"); continue
            key = next((owner[n] for n in numbers if n in owner), None)
            if key is None:
                key = min(numbers) if numbers else "email:" + min(emails)
                people[key] = {"names": set(), "numbers": set(), "emails": set()}
            p = people[key]
            p["names"].add(name); p["numbers"] |= numbers; p["emails"] |= emails
            for n in numbers:
                owner[n] = key
    return people, log


if __name__ == "__main__":
    sources = {
        "phone1": ["Dr. Ravi, +91 98400 12345, ravi@gmail.com", "Priya, 9876543210", "Ravi, 9123456789"],
        "phone2": ["ravi kumar, 9840012345; 044-24345678, RAVI@GMAIL.COM", "Priya S, 09876543210, priya@@mail"],
        "sim":    ["Anand, 99400 11111", "broken line without comma", "Priya, 98765 43210, priya.s@yahoo.in"],
    }
    people, log = merge(sources)
    for key, p in people.items():
        print(f"{key}: names={sorted(p['names'])} numbers={sorted(p['numbers'])} emails={sorted(p['emails'])}")
    print("log:", *log, sep="\n  ")
    print(f"{sum(len(v) for v in sources.values())} input lines -> {len(people)} people")
