from sys import stdin


n = int(input())

stack = []
for _ in range(n):
    command = stdin.readline().rstrip()
    if command[:4] == 'push':
        number = int(command.split()[1])
        stack.append(number)
    elif command == 'top':
        print(stack[-1]) if stack else print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1) if not stack else print(0)
    elif command == 'pop':
        print(stack.pop()) if stack else print(-1)
