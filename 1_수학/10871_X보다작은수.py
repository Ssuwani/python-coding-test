N, X = map(int, input().split())

numbers = list(map(int, input().split()))

[print(number, end=' ') for number in numbers if number < X]