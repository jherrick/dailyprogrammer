def dieroll(ndm):
	import random
	'''
	die = 0
	numroll = 0
	temp = ""
	result = ""

	for char in NdM:
		if char == "d":
			numroll = int(temp)
			temp = ""
		temp += char

	die = int(temp[1:])

	for roll in range(numroll):
		result += str(int(random.random()*die)) + " "

	return result
	'''
	rolls, sides = ndm.split('d')
	
	results = [str(random.randrange(1,int(sides)) for i in xrange(int(rolls))
	
	print(' '.join(results))

print dieroll("4d6")
