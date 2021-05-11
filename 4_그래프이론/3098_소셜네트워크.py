import copy
N, M = map(int, input().split())

relations = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    relations[A].append(B)
    relations[B].append(A)

cnt = 0
len_list = []
while True:
    cnt += 1
    len_start = sum([len(re) for re in relations])
    first = copy.deepcopy(relations)

    for i in range(1, N+1):
        for j in first[i]:
            for new_friends in first[j]:
                if (new_friends != i) and (new_friends not in first[i]):
                    relations[i].append(new_friends)
    relations = [list(set(relation)) for relation in relations]
    len_end = sum([len(re) for re in relations])
    len_list.append((len_end-len_start)//2)
    
    if len_end == N*(N-1):
        break

print(cnt)
[print(len_cnt) for len_cnt in len_list]