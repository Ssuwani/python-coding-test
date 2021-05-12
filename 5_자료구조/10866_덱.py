from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    command = input().split()
    if command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'front':
        print(q[0]) if q else print(-1)
    elif command[0] == 'back':
        print(q[-1]) if q else print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(1) if not q else print(0)
    elif command[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif command[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    
        