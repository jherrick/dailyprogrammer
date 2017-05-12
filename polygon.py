def polygon(n, r):
	import math

	s = 2 * math.sin(math.pi/n) * r

	CIRCUMFERENCE = s * n

	print "{0:.3f}".format(CIRCUMFERENCE)

polygon(5, 3.7)