n = int(input())

for _ in range(n):
    seq = input()
    open_cnt = 0
    close_cnt = 0
    fail = False
    for s in seq:
        if s == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        if close_cnt > open_cnt:
            fail = True
            break
    if open_cnt != close_cnt:
        fail = True
    if fail:
        print("NO")
    else:
        print("YES")
