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

x = [1, 2, 3]
y = [4, 5, 6]
assert list(zip(x, y)) == [(1, 4), (2, 5), (3, 6)]



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
	  1 2 3 4 5 6 7 8 9
	A
	B
	C
	D
	E
	F
	G
	H
	I
	"""

	numbers = '123456789'
	rows = 'ABCDEFGHI'
	cols = numbers

	def __init__(self, stringBoard):
		super(Board, self).__init__()
		self.stringBoard = stringBoard
		print (self.stringBoard)

		self.squares = []		
		self.unitList = []
		self.units = []
		self.peers = []

		self.__calculate_board()
		self.__test()		

	def __calculate_board(self):
		self.squares = self.__cross(Board.rows, Board.cols)
		self.unitList = ([self.__cross(Board.rows, c) for c in Board.cols] +
						 [self.__cross(r, Board.cols) for r in Board.rows] +
						 [self.__cross(r, c) for r in ("ABC", "DEF", "GHI") for c in ("123", "456", "789")])

		self.units = dict((s, [u for u in self.unitList if s in u]) for s in self.squares)		
		self.peers = dict((s, set(sum(self.units[s],[]))-set([s])) for s in self.squares)

	def __cross(self, A, B):
		"Cross product of elements in A and elements in B."
		return [a+b for a in A for b in B]

	def __grid_values(self):
		chars = [a for a in self.stringBoard if a in Board.numbers or a in ".0"]
		assert len(chars) == 81
		return dict(zip(self.squares, chars))

	def __assign(self, values, s, d):
		values = values
		other_values = values[s].replace(d, '')
		if all(self.__eliminate(values, s, d2) for d2 in other_values):
			return values
		else:
			return False

	def __eliminate(self, values, s, d):
		values = values
		"If number not exist in A1 : (123456789) "
		if d not in values[s]:
			return values
		values[s] = values[s].replace(d, '')

		if len(values[s]) == 0:
			return False
		elif len(values[s]) == 1:
			d2 = values[s]
			if not all(self.__eliminate(values, s2, d2) for s2 in self.peers[s]):
				return False

		for u in self.units[s]:
			dplace = [s for s in u if d in values[s]]
			if len(dplace) == 0:
				return False
			elif len(dplace) == 1:
				if not self.__assign(values, dplace[0], d):
					False
		return values

	def __test(self):
		"Test the calculated board"
		assert len(self.squares) == 81		
		assert len(self.unitList) == 27
		assert all(len(self.units[s]) == 3 for s in self.squares)
		assert all(len(self.peers[s]) == 20 for s in self.squares)
		assert self.units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
								    ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
								    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
		assert self.peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2','C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9','A1', 'A3', 'B1', 'B3'])
		print ("All tests pass.")

	def parse_grid(self):
		values = dict((s, self.cols) for s in self.squares)
		for s,d in self.__grid_values().items():
			if d in self.numbers and not self.__assign(values, s, d):
				return False ## (Fail if we can't assign d to square s.)
		return values


aVariable = Board('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
print (aVariable.parse_grid())
