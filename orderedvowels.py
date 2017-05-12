def ordered():
	file = open("enable1.txt", "r")
	words = file.readlines()

	vowels = "aeiouy"
	compare = ""

	for word in words:
		compare = ""
		if len(word) > len(vowels):
			for letter in word:
				if letter in vowels:
					compare += letter

		if compare == vowels:
			print word

ordered()


