horses = [107,47,102,64,50,100,28,91,27,5,22,114,23,42,13,3,93,8,92,79,53,83,63,7,15]

def horserace(horse):
	horses = horse
	races = [
			[],
			[],
			[],
			[],
			[]
			]
	temp = []
	fastest = []

	for race in range(len(horse)/5):
		current = horses[race*5:race*5+5]
		current.sort()
		for horse in range(2,5):
			races[race].append(current[horse])

	for race in range(len(races)):
		temp.append(races[race][4])

	for race in races:
		print race

horserace(horses)





