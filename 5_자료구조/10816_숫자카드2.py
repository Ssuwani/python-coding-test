import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())

cards = list(map(int, input().split()))

input()

nums = list(map(int, input().split()))
C = Counter(cards)
for num in nums:
    if num in C:
        print(C[num], end=' ')
    else:
        print(0, end=' ')
