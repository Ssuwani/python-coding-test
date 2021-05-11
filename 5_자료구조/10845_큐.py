from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    command = input().rstrip().split(" ")
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'front':
        print(q[0]) if q else print(-1)
    elif command[0] == 'back':
        print(q[-1]) if q else print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1) if not q else print(0)
    elif command[0] == 'pop':
        print(q.pop(0)) if q else print(-1)