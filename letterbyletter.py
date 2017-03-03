def letterbyletter(first, second):
	print first
	for letters in range(len(first)):
		if first[letters] != second[letters]:
			print second[:letters+1] + first[letters+1:]

letterbyletter("a fall to the floor", "braking the door in")