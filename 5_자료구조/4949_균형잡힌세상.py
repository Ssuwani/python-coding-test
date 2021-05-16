while True:
    sentence = input()
    ok = True
    if sentence == '.':
        break

    stack = []

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        
        elif s == ')':
            if not stack:
                ok = False
                break

            if stack[-1] == '(':
                stack.pop()
            else:
                ok = False
        
        elif s == ']':
            if not stack:
                ok = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                ok = False
    print("yes") if ok and not stack else print("no")