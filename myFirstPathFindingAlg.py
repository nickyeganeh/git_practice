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


#finds the shortest path from the bottom left of an array to the top left of the array
def findShortestPath(array):
	convertToBoolean(array)

	countMoves = 0
	r = len(array[0])
	c = 0

	try:
		while r != 0:
			if array[r-1][c] == False:
				countMoves += 1
				r -= 1

			elif array[r][c+1] == False:
				countMoves += 1
				c += 1

			elif array[r+1][c] == False:
				countMoves += 1
				r += 1

			if r == 0 and array[r][c-1] == False:
				countMoves += 1
				c -= 1
				
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
