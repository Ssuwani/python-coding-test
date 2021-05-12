from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

matrix = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

change = {}
l = int(input())

for _ in range(l):
    x, c = input().split()
    change[int(x)] = c

snake = deque([[0, 0]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1
times = 0
nx, ny = 0, 0


def boundary_check(x, y):
    return True if 0 <= x and x < n and 0 <= y and y < n else False

def change_direction(direction):
    global d
    if direction == 'D':
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d

while True:
    times += 1
    nx += dx[d]
    ny += dy[d]

    if times in change.keys():
        d = change_direction(change[times])

    if boundary_check(nx, ny):
        if [nx, ny] in snake:
            break
        if matrix[nx][ny] == 1:
            matrix[nx][ny] = 0
            snake.append([nx, ny])
        elif matrix[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break
print(times)


