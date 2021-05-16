n, m = map(int, input().split())
q = list(range(1, n+1))
nums = list(map(int, input().split()))
result = 0
for num in nums:
    left = q.index(num)
    right = q[::-1].index(num) + 1
    if left <= right:
        result += left
        for l in range(left):
            q.append(q.pop(0))
    else:
        result += right
        for r in range(right):
            q.insert(0, q.pop())
    q.pop(0)
print(result)
