def main(inps):
	checker = []
	roman = toRoman(inps)
	for letter in roman:
		if letter not in checker:
			checker.append(letter)

	if len(checker) == 7 and len(roman) == 7:
		print roman + ", " + str(inps)

def toRoman(inps):
	conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
           [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
           [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
           [   1, 'I']]
	roman = ""
	i = 0
	num = inps
	while num > 0:
		while conv[i][0] > num:
			i += 1
        	roman += conv[i][1]
        	num -= conv[i][0]

	return roman

if __name__ == '__main__':
	for x in range(2000):
		main(x)