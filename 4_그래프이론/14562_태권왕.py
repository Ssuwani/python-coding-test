n = int(input())


def fight(x, y, cnt):
    if (x > y):
        return True
    elif (x == y):
        answers.append(cnt)
        return cnt
    else:
        fight(x*2, y+3, cnt+1)
        fight(x+1, y, cnt+1)


for _ in range(n):
    answers = []
    x, y = map(int, input().split())
    fight(x, y, 0)
    print(min(answers))
