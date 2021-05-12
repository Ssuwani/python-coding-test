from collections import deque
n = int(input())

cards = list(range(1, n+1))
q = deque(cards)
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
    # print(cards)
print(q[0])
