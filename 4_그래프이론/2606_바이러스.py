computer = int(input())
n = int(input())
relations = [[] for _ in range(computer+1)]
visited = []
for _ in range(n):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

def dfs(start, relations):
    for i in relations[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, relations)

dfs(1, relations)
print(len(visited)-1)
