def pangram(sentence):
	
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	letters = []

	for letter in sentence:
		if letter not in letters and letter.isalpha():
			letters += letter.lower()

	print sorted(letters)

	if sorted(letters) == alpha:
		return True

	return False


print pangram("The quick brown fox jumps over the lazy dog.")
print pangram("Pack my box with five dozen liquor jugs")
print pangram("Saxophones quickly blew over my jazzy hair")