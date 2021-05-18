n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[False]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j, visited, index):
    visited[i][j] = True
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                graph[nx][ny] = index
                dfs(nx, ny, visited, index)


index = 2
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 0:
            graph[i][j] = index
            dfs(i, j, visited, index)
            index += 1

print(graph)