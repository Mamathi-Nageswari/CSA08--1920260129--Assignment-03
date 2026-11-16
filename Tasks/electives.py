"""Q4 - Elective clash detection with sets (Complete the Code)."""
ai_elective = {"192311001", "192311004", "192311007", "192311009"}
iot_elective = {"192311002", "192311004", "192311009", "192311010"}
all_students = {f"1923110{i:02d}" for i in range(1, 11)}

# TODO 1
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("clash :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither :", sorted(neither))

m_both = ai_elective.intersection(iot_elective)
m_one = ai_elective.symmetric_difference(iot_elective)
m_neither = all_students.difference(ai_elective.union(iot_elective))
print("methods give the same results:", (m_both, m_one, m_neither) == (both, exactly_one, neither))

registrations = ["192311001", "192311004", "192311001", "192311007"]
print("with duplicates:", registrations, "-> set:", sorted(set(registrations)))
print("empty elective clash:", set() & iot_elective, "| identical electives exactly one:", ai_elective ^ set(ai_elective))
print("set of tuples ok:", {("192311001", "AI")})
try:
    {["192311001", "AI"]}
except TypeError as e:
    print("set of lists ->", e)
