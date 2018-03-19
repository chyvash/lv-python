alphabet = ' abcdefghiklmnoprstuvwxyz'
s = input().strip()
res = ''
n = 0
print('Example of decoding: ')
while n < 25:
	for c in s:
		res += alphabet[(alphabet.index(c) + n) % len(alphabet)]
	n += 1
	print('"' + res + '"')
	res = ''