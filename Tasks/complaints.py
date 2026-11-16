"""Q3 - Kisan call centre: word frequencies, grouping, top k (Complete the Code)."""
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}


def frequencies(texts, stop):
    # TODO 1
    counts = {}
    for text in texts:
        for word in text.lower().split():
            word = word.strip(".,!?;:")
            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts


def top(counts, k):
    # TODO 2
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]


if __name__ == "__main__":
    print(top(frequencies(calls, STOP), 3))
    records = [("Thanjavur", "paddy", "seeds not received"), ("Madurai", "cotton", "pest attack"),
               ("Thanjavur", "banana", "price low"), ("Salem", "paddy", "water shortage")]
    by_district, by_crop = {}, {}
    for district, crop, text in records:
        by_district.setdefault(district, []).append(text)
        by_crop.setdefault(crop, []).append(text)
    print("complaints per district:", {d: len(v) for d, v in by_district.items()})
    print("by crop:", by_crop)
    print("empty text:", frequencies([], STOP), "| case/punctuation:",
          frequencies(["Seeds, SEEDS. seeds!"], STOP))
    d = frequencies(calls, STOP)
    print("keys  :", list(d.keys()))
    print("values:", list(d.values()))
    print("items :", list(d.items())[:3], "...")
