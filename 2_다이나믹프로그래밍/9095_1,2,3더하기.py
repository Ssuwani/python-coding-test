n = int(input())
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
def get_cases_num(n):
    if d[n]:
        return d[n]
    else:
        d[n] = get_cases_num(n-1) + get_cases_num(n-2) + get_cases_num(n-3)
        return d[n]

[print(get_cases_num(int(input()))) for _ in range(n)]

