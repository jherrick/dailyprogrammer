def unshared_copy(inList):
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList

def zeromatrix(matr):
	import copy
	height = len(matr)
	width = len(matr[0])

	dummy = unshared_copy(matr)

	for y in range(height):
		for x in range(width):
			if matr[y][x] == 0:
				for j in range(width):
					dummy[y][j] = 0
					#print "flipping " + str(y) + str(j)
				for k in range(height):
					dummy[k][x] = 0

	for height in range(height): 
		print dummy[height]

test1 = [[0,1],[1,1]]


zeromatrix(test1)

