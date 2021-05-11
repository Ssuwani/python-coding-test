n, k = map(int, input().split())
seq = list(range(1, n+1))

index = 0
result = []

for i in range(n):
    index += k - 1
    if len(seq) < index + 1:
        index %= len(seq)
    result.append(seq.pop(index))
print(str(result).replace("[", "<").replace("]", ">"))
