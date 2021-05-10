n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j, each in enumerate(graph[i]):
        if j == 0:
            graph[i][j] += graph[i-1][0]
        elif j == len(graph[i]) - 1:
            graph[i][j] += graph[i-1][-1]
        else:
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])

print(max(graph[-1]))
