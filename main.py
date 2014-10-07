# Ints
print (1 + 1)

# string
print ("Print a string")

# String + int WOW!!!
print ("Print this string with this int: " + str(1)) 

# This you can't do in C#!!! WOW!!!
print ([1, "I'm in the middle of this array?!?!?", 0])

# Python is so awesome!!!
array = [1, 2, 3, 4, 5] 
print ([(str(c) + "python") for c in array])

print ([i for i in array if i != 5])



stringBoard = """
4 . . |. . . |8 . 5 
. 3 . |. . . |. . . 
. . . |7 . . |. . . 
------+------+------
. 2 . |. . . |. 6 . 
. . . |. 8 . |4 . . 
. . . |. 1 . |. . . 
------+------+------
. . . |6 . 3 |. 7 . 
5 . . |2 . . |. . . 
1 . 4 |. . . |. . . 
"""


class Board():
	"""
	  A B C D E F G H I
	1
	2
	3
	4
	5
	6
	7
	8
	9
	"""

	numbers = '123456789'
	letters = 'ABCDEFGHI'

	def __init__(self, stringBoard):
		super(Board, self).__init__()
		self.stringBoard = stringBoard
		self.printStringBoard()
		self.calculateSquares()
		self.calculateRows()
		self.calculateColumns()

	def printStringBoard(self):
		print (self.stringBoard)
	
	def calculateSquares(self):
		self.squares = [self.cross(cols, rows) for cols in ("ABC", "DEF", "GHI") for rows in ("123", "456", "789")]
		print (self.squares[0])

	def calculateRows(self):
		self.rows = [self.cross(rows, Board.letters) for rows in Board.numbers]

	def calculateColumns(self):
		self.columns = [self.cross(Board.numbers, cols) for cols in Board.letters]

	def cross(self, A, B):
		"Cross product of elements in A and elements in B."
		return [a+b for a in A for b in B]

		
aVariable = Board(stringBoard)
