def dfs(sample):
    for other, mark in checks[sample]:
        current_type = groups[sample]
        next_type = current_type ^ mark

        if groups[other] == -1:
            groups[other] = next_type

            result = dfs(other)
            if result == False:
                return False
        else:
            if groups[other] != next_type:
                return False

    return True


first_line = input().split()
count_samples = int(first_line[0])
count_checks = int(first_line[1])

checks = []
for i in range(count_samples + 1):
    checks.append([])

for i in range(count_checks):
    row = input().split()

    left_sample = int(row[0])
    right_sample = int(row[1])
    mark = int(row[2])

    checks[left_sample].append((right_sample, mark))
    checks[right_sample].append((left_sample, mark))

groups = []
for i in range(count_samples + 1):
    groups.append(-1)

answer = True

for sample in range(1, count_samples + 1):
    if groups[sample] == -1:
        groups[sample] = 0

        result = dfs(sample)

        if result == False:
            answer = False
            break

if answer == True:
    print("YES")
else:
    print("NO")