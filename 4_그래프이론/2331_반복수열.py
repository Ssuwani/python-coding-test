A, P = map(int, input().split())

seq = [A]

while True:
    new_num = sum([int(num)**P for num in str(seq[-1])])
    if new_num in seq:
        result = seq.index(new_num)
        break
    seq.append(new_num)

print(result)