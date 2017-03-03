def scrabble(tiles, word):
	if tiles == word:
		return True
	tracker = {}
	tracker["?"] = 0
	for letters in tiles:
		if letters in tracker:
			tracker[letters] += 1
		else:
			tracker[letters] = 1

	for letters in word:
		if letters in tracker and tracker[letters] > 0:
			tracker[letters] -= 1
		elif tracker["?"] > 0:
			tracker["?"] -= 1
		else:
			return False
	return True

def longest(letters):
	file = open("enable1.txt", "r")
	words = file.readlines()

	words = sorted(words, key=len)
	for word in reversed(words):
		word = word.lower().strip()
		if len(word) <= len(letters):
			isValid = scrabble(letters, word)
			if isValid:
				return word

def highest(letters):
	file = open("enable1.txt")
	words = file.readlines()

	highscoreword = ""
	highscore = 0
	for word in words:
		word = word.lower().strip()
		if len(word) <= len(letters):
			isValid = scrabble(letters, word)
			if isValid:
				if scored(word) > highscore:
					highscore = scored(word)
					highscoreword = word
	return highscoreword

def scored(word):
	scores = {"e":1, "a":1, "i":1, "o":1, "n":1, "r":1, "t":1, "l":1, "s":1, "u":1, "d":2, "g":2, "b":3, "c":3, "m":3, "p":3, "f":4, "h":4, "v":4, "w":4, "y":4, "k":5, "j":8, "x":8, "q":10, "z":10, "?":0}
	score = 0
	for letters in word:
		score += scores[letters]
	return score

print highest("dcthoyueorza") 
print highest("uruqrnytrois") 
print highest("rryqeiaegicgeo??")
print highest("udosjanyuiuebr??") 
print highest("vaakojeaietg????????") 

