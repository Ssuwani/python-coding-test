op = input()
start_pipe = []
answer = 0
for o in op:
    if o == '(':
        start_pipe.append(o)
        last = o
    else:
        start_pipe.pop()
        if last == "(":
            answer += len(start_pipe)
            last = o
        else:
            answer += 1
print(answer)
