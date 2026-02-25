capacity = {
    "A": 2,
    "B": 1
}

student_pref = {
    "s1": ["A", "B"],
    "s2": ["A", "B"],
    "s3": ["B", "A"]
}

hospital_pref = {
    "A": ["s2", "s1", "s3"],
    "B": ["s1", "s3", "s2"]
}

hospital_matches = {
    "A": [],
    "B": []
}

next_choice = {
    "s1": 0,
    "s2": 0,
    "s3": 0
}

free_students = ["s1", "s2", "s3"]

def hospital_prefers(hospital, s1, s2):
    prefs = hospital_pref[hospital]
    return prefs.index(s1) < prefs.index(s2)

while free_students:
    student = free_students.pop(0)

    if next_choice[student] >= len(student_pref[student]):
        continue

    hospital = student_pref[student][next_choice[student]]
    next_choice[student] += 1

    if len(hospital_matches[hospital]) < capacity[hospital]:
        hospital_matches[hospital].append(student)
    else:
        worst = hospital_matches[hospital][0]
        for s in hospital_matches[hospital]:
            if hospital_prefers(hospital, worst, s):
                worst = s

        if hospital_prefers(hospital, student, worst):
            hospital_matches[hospital].remove(worst)
            hospital_matches[hospital].append(student)
            free_students.append(worst)
        else:
            free_students.append(student)

print("Распределение:")
for h in hospital_matches:
    print(h, ":", hospital_matches[h])