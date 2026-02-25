men_prefs = {
    "m1": ["w1", "w2", "w3"],
    "m2": ["w2", "w1", "w3"],
    "m3": ["w1", "w2", "w3"]
}

women_prefs = {
    "w1": ["m2", "m1", "m3"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m1", "m2", "m3"]
}

rank = {}
for w in women_prefs:
    rank[w] = {}
    for i in range(len(women_prefs[w])):
        rank[w][women_prefs[w][i]] = i

match_w = {}
match_m = {}
next_choice = {}
free_men = []

for m in men_prefs:
    next_choice[m] = 0
    free_men.append(m)

while len(free_men) > 0:
    m = free_men.pop(0)

    if next_choice[m] >= len(men_prefs[m]):
        continue

    w = men_prefs[m][next_choice[m]]
    next_choice[m] += 1

    if w not in match_w:
        match_w[w] = m
        match_m[m] = w
    else:
        m2 = match_w[w]
        if rank[w][m] < rank[w][m2]:
            match_w[w] = m
            match_m[m] = w
            del match_m[m2]
            free_men.append(m2)
        else:
            free_men.append(m)

print("Честный матчинг:", match_w)

true_women_prefs = {}
for w in women_prefs:
    true_women_prefs[w] = women_prefs[w][:]

found = False

for w in true_women_prefs:
    r = {}
    for i in range(len(true_women_prefs[w])):
        r[true_women_prefs[w][i]] = i

    old_partner = match_w[w]
    old_rank = r[old_partner]

    n = len(true_women_prefs[w])

    for i in range(n):
        for j in range(i + 1, n):

            women_prefs = {}
            for ww in true_women_prefs:
                women_prefs[ww] = true_women_prefs[ww][:]

            a = women_prefs[w][i]
            b = women_prefs[w][j]
            women_prefs[w][i] = b
            women_prefs[w][j] = a

            rank = {}
            for ww in women_prefs:
                rank[ww] = {}
                for k in range(len(women_prefs[ww])):
                    rank[ww][women_prefs[ww][k]] = k

            match_w2 = {}
            match_m2 = {}
            next_choice = {}
            free_men = []

            for m in men_prefs:
                next_choice[m] = 0
                free_men.append(m)

            while len(free_men) > 0:
                m = free_men.pop(0)

                if next_choice[m] >= len(men_prefs[m]):
                    continue

                ww = men_prefs[m][next_choice[m]]
                next_choice[m] += 1

                if ww not in match_w2:
                    match_w2[ww] = m
                    match_m2[m] = ww
                else:
                    m2 = match_w2[ww]
                    if rank[ww][m] < rank[ww][m2]:
                        match_w2[ww] = m
                        match_m2[m] = ww
                        del match_m2[m2]
                        free_men.append(m2)
                    else:
                        free_men.append(m)

            new_partner = match_w2[w]
            new_rank = r[new_partner]

            if new_rank < old_rank:
                print("Женщина:", w)
                print("Поменяла местами:", a, b)
                print("Было:", old_partner)
                print("Стало:", new_partner)
                found = True
                break

        if found:
            break
    if found:
        break

if not found:
    print("Улучшений не найдено")