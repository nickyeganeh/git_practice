'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
array1 = [['f', 'f', 'f', 'f'],
		  ['t', 't', 'f', 't'],
		  ['f', 'f', 'f', 'f'],
		  ['f', 'f', 'f', 'f']]

array2 = [['f', 'f', 'f', 'f'],
		  ['t', 't', 't', 't'],
		  ['f', 'f', 'f', 'f'],
		  ['f', 'f', 'f', 'f']]

array3 = [['f', 'f', 'f', 'f'],
		  ['t', 't', 'f', 't'],
		  ['t', 'f', 'f', 'f'],
		  ['f', 't', 'f', 'f']]

array4 = [['f', 'f', 'f', 'f'],
		 ['t', 't', 't', 'f'],
		 ['f', 'f', 'f', 'f'],
		 ['f', 'f', 'f', 'f']]

#converts t's and f's to True and False boolean values		
def convertToBoolean(array):	
	r = 0
	while r < len(array[0]):
		c = 0
		while c < len(array):
			if array[r][c] == 't':
				array[r][c] = True
			else:
				array[r][c] = False
			c += 1
		r += 1


def isPathAvailable(array):
	pathFound = True
	for i in array:
		if len(set(i)) == 1:
			pathfound = False
		else:
			pathFound = True
	return pathFound

#finds the shortest path from the bottom left of an array to the top left of the array
def findShortestPath(array):
	try:
		convertToBoolean(array)
		pathFound = True
		countMoves = 0
		r = len(array[0])
		c = 0
		while r != 0 and isPathAvailable(array) and pathFound:
			if array[r-1][c] == False:
				r -= 1
				countMoves += 1

			elif array[r][c+1] == False:
				c += 1
				countMoves += 1

			elif array[r+1][c] == False:
				r += 1
				countMoves += 1

			elif array[r][c+1] == True and array[r-1][c] == True:
				pathFound = False
				break
			
			if r == 0 and array[r][c-1] == False:
				c -= 1
				countMoves += 1

			elif r == 0 and array[r][c-1] == True:
				pathFound = False

		if isPathAvailable(array) and pathFound:
			return countMoves
		else:
			countMoves = "Path not found."
			return countMoves

	except IndexError as e:
		countMoves = "Path not found."
		return countMoves
	

shortestPath1 = findShortestPath(array1)
print("The shortest path for array1 is:",shortestPath1)

shortestPath2 = findShortestPath(array2)
print("The shortest path for array2 is:",shortestPath2)

shortestPath3 = findShortestPath(array3)
print("The shortest path for array3 is:",shortestPath3)

shortestPath4 = findShortestPath(array4)
print("The shortest path for array4 is:",shortestPath4)
