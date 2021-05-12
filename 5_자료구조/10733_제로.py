n = int(input())
stack = []
for _ in range(n):
    x = int(input())
    if x:
        stack.append(x)
    else:
        stack.pop()
    
print(sum(stack))