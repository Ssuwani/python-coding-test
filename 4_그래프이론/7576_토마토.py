from collections import deque

m, n = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
q = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    while len(q)  !=0 :
        # print(q)
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if s[nx][ny] == 0:
                s[nx][ny] = s[x][y] + 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            q.append((i,j))
# print(q)
bfs()

from functools import reduce

s = reduce(lambda x,y:x+y, s)
if 0 in s:
    print(-1)
else:
    if max(s) == 1:
        print(0)
    else:
        print(max(s)-1)