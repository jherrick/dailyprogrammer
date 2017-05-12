def fallout():
	import random
	difficulty = {"1":4,"2":5,"3":6,"4":7,"5":8}

	playerinput = 0
	while playerinput < 1:
		print "Difficulty (1-5)? "
		checked = raw_input()
		if checked not in difficulty:
			print "Please input a number 1-5"
		else:
			playerinput = checked

	pwords = getwords(difficulty[playerinput])

	for word in pwords:
		print word

	answer = random.choice(pwords)

	guess = 4
	while guess != 0:	
		print "Guess (%d left)?" % (guess)
		playerguess = raw_input()
		print "%d/%d correct" % (checkguess(answer, playerguess), len(answer))
		guess -= 1
		if playerguess == answer:
			print "You Win!"
			break

	if guess == 0:
		print "You lose, the word was " + answer + " ."
		
def getwords(length):
	import random
	file = open("enable1.txt", "r")
	words = file.readlines()

	options = []
	passwords = []

	for word in words:
		word = word.lower().strip()
		if len(word) == length:
			options.append(word)

	for choices in range(10):
		passwords.append(random.choice(options))

	return passwords


def checkguess(answer, guess):
	result = 0
	for x in range(len(guess)):
		if guess[x] == answer[x]:
			result += 1
	return result

fallout()

