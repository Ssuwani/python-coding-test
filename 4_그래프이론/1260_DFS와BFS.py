from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

[g.sort() for g in graph]


def dfs(visited, graph, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(visited, graph, i)


def bfs(visited, graph, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False] * (N+1)
dfs(visited, graph, V)
print()
visited = [False] * (N+1)
bfs(visited, graph, V)
