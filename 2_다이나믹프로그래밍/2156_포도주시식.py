n = int(input())
beverage = [0]
for _ in range(n):
    beverage.append(int(input()))

dp = [0]
dp.append(beverage[1])
if n > 1:
    dp.append(beverage[1]+beverage[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2]+beverage[i],
              dp[i-3]+beverage[i-1]+beverage[i]))

print(dp[n])
