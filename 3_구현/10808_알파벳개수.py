word = input()
chrs = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(*[word.count(chr) for chr in chrs], sep=' ')
