n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n//5
        n -= 5 * (n//5)
    else:
        result += 1
        n -= 3
        if n < 0:
            print(-1)
            exit()

print(result)
