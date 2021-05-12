n = int(input())
stack = []
result = []
count = 0
no_message = True
for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        break
if not no_message:
    print("NO")
else:
    print("\n".join(result))
