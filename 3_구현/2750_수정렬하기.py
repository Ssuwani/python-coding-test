n = int(input())

seq = [int(input()) for _ in range(n)]

seq.sort()
seq = [str(s) for s in seq]
print("\n".join(seq))