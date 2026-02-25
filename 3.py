from itertools import permutations

ratings_A = [8, 5, 1]
ratings_B = [7, 6, 2]

all_A = list(permutations(ratings_A))
all_B = list(permutations(ratings_B))

result = None
n = len(ratings_A)

for S in all_A:
    for T in all_B:
        current = 0
        for a, b in zip(S, T):
            if a > b:
                current += 1

        best_A = current
        for S2 in all_A:
            w = 0
            for a, b in zip(S2, T):
                if a > b:
                    w += 1
            if w > best_A:
                best_A = w

        if best_A > current:
            continue

        current_B = n - current
        best_B = current_B

        for T2 in all_B:
            w = 0
            for a, b in zip(S, T2):
                if a > b:
                    w += 1
            b_score = n - w
            if b_score > best_B:
                best_B = b_score

        if best_B > current_B:
            continue

        result = (S, T)
        break
    if result is not None:
        break

if result is None:
    print("Устойчивая пара расписаний не найдена")
else:
    print("S (A):", result[0])
    print("T (B):", result[1])