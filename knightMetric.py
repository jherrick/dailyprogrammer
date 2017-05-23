'''
A knight piece in chess can only make L-shaped moves. Specifically, it can only move x steps to the right 
and y steps up if (x,y) is one of:

(-1,-2) ( 1,-2) (-1, 2) ( 1, 2)
(-2,-1) ( 2,-1) (-2, 1) ( 2, 1)

(For this problem, assume the board extends infinitely in all directions, 
so a knight may always make eight moves from any starting point.) A knight starting from (0,0) 
can reach any square, but it may have to take a roundabout route. For instance, to reach the square (0,1) 
requires three steps:

 2,  1
-1,  2
-1, -2

Write a program, that, given a square (x,y), returns how many moves it takes a knight to reach that 
square starting from (0,0).
'''
def knightMetric(data):
	a,b = data.split(' ')
	target = [a,b]
	visited = [[False for x in range(30)] for y in range(30)]
	count = 0
	BFS(0, 0, visited, count, target)

def BFS(x, y, visited, count, target):
	neighbors = [[-1,-2], [1,-2], [-1,2], [1,2], [-2,-1], [2,-1], [-2,1], [2, 1]]

	visited[x][y] = True

	count += 1
	if x == target[0] and y == target[1]:
		print count

	#need to fix out of range error
	for e in range(8):
		if (x+neighbors[e][0])<29 and (y+neighbors[e][1])<29:
			if not visited[x+neighbors[e][0]][y+neighbors[e][1]]:
				return BFS(x+neighbors[e][0],y+neighbors[e][1],visited,count,target)

if __name__ == '__main__':
	knightMetric("3 7")




