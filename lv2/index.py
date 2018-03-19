while 1:
	print("Выберите шифровать(1) или дешифровать строку(2), 0 - закрыть ")
	flag = input()
	alphabet = ' abcdefghiklmnoprstuvwxyz'
	if flag == '1':
		print("Введите сдвиг для шифрования")
		n = int(input())
		print("Введите строку")
		s = input().strip()
		res = ''
		for c in s:
			res += alphabet[(alphabet.index(c) + n) % len(alphabet)]
		print('Result: "' + res + '"')
	elif flag == '2':
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
	elif flag == '0':
		break;