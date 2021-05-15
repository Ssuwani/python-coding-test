seq = list(map(int, input().split()))

if seq == list(range(1, 9)):
    print("ascending")
elif seq == list(range(1, 9))[::-1]:
    print("descending")
else:
    print("mixed")