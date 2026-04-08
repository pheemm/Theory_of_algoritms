from collections import deque

def check_consistency(n, constraints):
    graph = [[] for _ in range(n + 1)]
    for i, j, relation in constraints:
        t = 0 if relation == "same" else 1
        graph[i].append((j, t))
        graph[j].append((i, t))

    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])

        while q:
            v = q.popleft()
            for u, t in graph[v]:
                need = color[v] ^ t
                if color[u] == -1:
                    color[u] = need
                    q.append(u)
                elif color[u] != need:
                    return False, None

    return True, color

n = 5
constraints = [
    (1, 2, "same"),
    (2, 3, "diff"),
    (3, 4, "same"),
    (4, 5, "diff"),
    (1, 5, "diff")
]

ok, color = check_consistency(n, constraints)

if ok:
    print("Оценки непротиворечивы")
    for i in range(1, n + 1):
        print(i, "A" if color[i] == 0 else "B")
else:
    print("Оценки противоречивы")