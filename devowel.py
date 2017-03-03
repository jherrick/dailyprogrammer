def devowel(string):
	text = string.replace(" ","")
	vowels = 'aeiou'
	print "".join(char for char in text if char not in vowels)
	print "".join(char for char in text if char in vowels)

devowel("all those who believe in psychokinesis raise my hand")