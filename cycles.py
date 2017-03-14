def main():
	base = int(raw_input())
	num = raw_input()

	cycle = []

	while True:
		temp = [int(i) for i in str(num)]
		num2 = 0
		for numb in temp:
			num2 += numb**base
		if num2 not in cycle:
			cycle.append(num2)
		else:
			return cycle[cycle.index(num2):]
			break
		num = num2

if __name__ == '__main__':
	print main()