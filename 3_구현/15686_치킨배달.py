from itertools import combinations
n,m = map(int, input().split())
graph = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j, d in enumerate(data):
        if d == 2:
            chicken.append((i,j))

delete = list(combinations(chicken, len(chicken) - m))
min_value = int(1e9)
for ds in delete:
    # print("here", ds)
    for d in ds:
        graph[d[0]][d[1]] = -1
    value = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house_chicken_distance = int(1e9)
                for chi in chicken:
                    if chi not in ds:
                        distance = abs(chi[0]-i) + abs(chi[1]-j)
                        house_chicken_distance = min(house_chicken_distance, distance)
                value += house_chicken_distance
                # print(i,j,house_chicken_distance)
    if value < min_value:
        min_value = value

    for d in ds:
        graph[d[0]][d[1]] = 2
print(min_value)