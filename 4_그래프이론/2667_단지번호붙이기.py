n = int(input())
ap = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
answer = []
visited = [[False]*n for _ in range(n)]


def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] == False and ap[nx][ny] == 1:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if ap[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)
print(len(answer))
[print(ans) for ans in answer]
