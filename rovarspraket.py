def rovarspraket(string):
	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	result = ""
	for letters in string:
		if letters not in vowels and letters.isalpha():
			result += letters + "o" + letters.lower()
		else:
			result += letters

	return result

print rovarspraket("I'm speaking Robber's language!")