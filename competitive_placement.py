import time

def is_safe(v, selected_nodes, graph):
    if v in selected_nodes:
        return False
    
    for neighbor in graph[v]:
        if neighbor in selected_nodes:
            return False
        
    return True

def can_p2_win(selected, p2_score, turn_p1):
    available = []
    for v in graph:
        if is_safe(v, selected, graph):
            available.append(v)

    if not available:
        return p2_score >= target_B
    
    if turn_p1:
        for move in available:
            if not can_p2_win(selected + [move], p2_score, False):
                return False
        return True
    
    else:
        for move in available:
            if can_p2_win(selected + [move], p2_score + weights[move], True):
                return True
        return False

graph = {0 :[1],
         1 :[0, 2],
         2 :[1, 3],
         3 :[2, 4],
         4 :[3, 5],
         5 :[4, 6],
         6 :[5, 7],
         7 :[6, 8],
         8 :[7, 9],
         9 :[8]}

weights = [10, 1, 5, 15, 5, 1, 5, 1, 15, 10]

target_B = 25

start = time.perf_counter()

print(can_p2_win([], 0, True))

finish = time.perf_counter()
print(f"Время{finish - start}")