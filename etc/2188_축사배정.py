N, M = map(int, input().split())


info = []

group_a, group_b = [-1] * N, [-1] * M

for i in range(N):
    list_tmp = list(map(int, input().split()))
    info.append(list_tmp[1:])


def dfs(a):
    visit[a] = True

    for b in info[a]:
        b -= 1
        if group_b[b] == -1 or not visit[group_b[b]] and dfs(group_b[b]):
            group_a[a], group_b[b] = b, a  # 축사 배정
            return True
    return False


count = 0

for i in range(N):
    if group_a[i] == -1:
        visit = [False] * N
        if dfs(i):
            count += 1

print(count)
