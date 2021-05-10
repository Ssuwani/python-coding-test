n = int(input())

waiting = list(map(int, input().split()))

waiting.sort(reverse=True)

print(sum([(i+1)*time for i, time in enumerate(waiting)]))
