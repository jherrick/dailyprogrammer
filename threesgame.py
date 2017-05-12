def threesgame(number):
	numba = number

	while numba != 1:
		print "%d %d" % (numba, (0, -1, 1)[numba % 3])
		numba = (numba + (0, -1, 1)[numba % 3]) / 3

	print 1

threesgame(100)