n = int(input())
houses = list(map(float, input().split()))

houses.sort()

stations = []
i = 0

while i < n:
    left_house = houses[i]

    station = left_house + 4
    stations.append(station)

    cover_right = station + 4

    while i < n and houses[i] <= cover_right:
        i += 1

print(n, houses)
print(len(stations))
print(*stations)