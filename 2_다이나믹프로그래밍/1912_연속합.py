n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * (n+1)
result = -1001
for i in range(n):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    result = max(result, dp[i])

print(result)