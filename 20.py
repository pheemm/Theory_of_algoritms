n = int(input())

people = []

for i in range(n):
    swim, bike, run = map(int, input().split())
    tail = bike + run
    people.append((i + 1, swim, bike, run, tail))

people.sort(key=lambda x: x[4], reverse=True)

current_time = 0
finish_time = 0
order = []

for person in people:
    number, swim, bike, run, tail = person

    current_time += swim
    total_finish = current_time + bike + run

    finish_time = max(finish_time, total_finish)
    order.append(number)

print("Оптимальный порядок:")
print(*order)

print("Минимальное завершающее время:")
print(finish_time)