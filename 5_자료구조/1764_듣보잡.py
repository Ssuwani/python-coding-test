from collections import Counter
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

result = [i for i,v in Counter(a+b).items() if v == 2]
result.sort()
print(len(result))

print('\n'.join(result))

