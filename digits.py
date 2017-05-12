def digits(number):
	while number > 9:
		s = 0
		while number > 0:
			s += number%10
			number = number/10
		number = s
	return number

print digits(31337)
print digits(1073741824)
print digits(9)