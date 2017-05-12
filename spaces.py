#write message to replace all spaces in strings with %20

def space(string, length):
	answer = ""
	for letters in range(length):
		if string[letters] == " ":
			answer += "%20"
		else:
			answer += string[letters]
	return answer

print space("mr john smith    ", 13)