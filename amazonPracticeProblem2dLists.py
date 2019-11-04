'''
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

og.		modified
1		 1
2		 2
3		 3
4		 4
5		 5
10		 10
15		 9
20		 8
19		 7
18		 6
17		 11
16		 12
11		 13 
6		 14
7		 15
8		 20
9		 19
14		 18
13		 17
12		 16
'''
given = [[1,  2,  3,  4,  5],
 		[6,  7,  8,  9,  10],
 		[11, 12, 13, 14, 15],
 		[16, 17, 18, 19, 20]]
print(given)

i = 0
while i < len(given):
	if i % 2 == 0:
		for j in given[i]:
			print (j)

	else:
		j = len(given[i]) - 1
		while j >= 0:
			print(given[i][j])
			j -= 1
	i += 1
