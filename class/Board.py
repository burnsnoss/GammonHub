import Piece
import Point

class Board:
	board = {}
	
	p1Color = ''
	p2Color = ''
	p1Score = 0
	p2Score = 0
	p1Bank = 0
	p2Bank = 0

	printedBoard = ['_____________________________________________________________________',
	'_____________________________________________________________________',
	'    13   14   15   16   17   18       19   20   21   22   23   24    ',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ]  V    V    V    V    V    V  [ ]  V    V    V    V    V    V  [ ]',
	'[ ]                              [ ]                              [ ]',
	'[ ]                              [ ]                              [ ]',
	'[ ]                              [ ]                              [ ]',
	'[ ]  A    A    A    A    A    A  [ ]  A    A    A    A    A    A  [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'[ ] | |  | |  | |  | |  | |  | | [ ] | |  | |  | |  | |  | |  | | [ ]',
	'____12___11___10____9____8____7_______6____5____4____3____2____1_____',
	'_____________________________________________________________________']

	# pointPrintOrder = [13,12,14,11,15,10,16,9,17,8,18,7,19,6,20,5,21,4,22,3,23,2,24,1]

	pointPrintCoords = {
		1:  (17, 63),
		2:  (17, 58),
		3:  (17, 53),
		4:  (17, 48),
		5:  (17, 43),
		6:  (17, 38),
		7:  (17, 30),
		8:  (17, 25),
		9:  (17, 20),
		10: (17, 15),
		11: (17, 10),
		12: (17, 5),
		13: (3, 5),
		14: (3, 10),
		15: (3, 15),
		16: (3, 20),
		17: (3, 25),
		18: (3, 30),
		19: (3, 38),
		20: (3, 43),
		21: (3, 48),
		22: (3, 53),
		23: (3, 58),
		24: (3, 63)
	}

	def __init__(self, color):
		# Set player colors
		self.p1Color = color 
		if color == 'w':
			self.p2Color = 'b'
		else:
			self.p2Color = 'w'

		# Put pieces on the board in starting arrangement
		for i in range(1,25):
			self.board[i] = Point.Point(i)
			if i == 1:
				for j in range(2):
					self.board[i].addPiece(Piece.Piece(self.p2Color))
			if i == 6:
				for j in range(5):
					self.board[i].addPiece(Piece.Piece(self.p1Color))
			if i == 8:
				for j in range(3):
					self.board[i].addPiece(Piece.Piece(self.p1Color))
			if i == 12:
				for j in range(5):
					self.board[i].addPiece(Piece.Piece(self.p2Color))
			if i == 13:
				for j in range(5):
					self.board[i].addPiece(Piece.Piece(self.p1Color))
			if i == 17:
				for j in range(3):
					self.board[i].addPiece(Piece.Piece(self.p2Color))
			if i == 19:
				for j in range(5):
					self.board[i].addPiece(Piece.Piece(self.p2Color))
			if i == 24:
				for j in range(2):
					self.board[i].addPiece(Piece.Piece(self.p1Color))


	'''
		splitPrintedBoard - splits the printed board into a list of lists for easier manipulation
	'''
	def splitPrintedBoard(self):
		# Splits the printed board into a list of lists
		#  For easier mainuplation and printing
		finalResult = []
		line = []

		for row in self.printedBoard:
			for char in row:
				line.append(char)
			finalResult.append(line)
			line = []

		return finalResult


	'''
		printBoard - prints the board based on what's in the board variable
	'''
	def printBoard(self):
		splitBoard = self.splitPrintedBoard()

		for i in range(1,25):
			pcs = self.board[i].getPieces()
			row, col = self.pointPrintCoords[i]
		
			numPcs = 0

			for piece in pcs:
				splitBoard[row][col] = piece.printPiece()
				if i < 13:
					row -= 1
				else:
					row += 1

				numPcs += 1

				if numPcs == 5:
					break

			if len(pcs) > 5:
				if i < 13:
					row -= 1
				else:
					row += 1

				numPcs = str(len(pcs))

				if len(numPcs) > 1:
					splitBoard[row][col+1] = numPcs[1]
				splitBoard[row][col] = numPcs[0]

		printLine = ''

		for line in splitBoard:
			for char in line:
				printLine += char
			print printLine
			printLine = ''

		print ' '


	def validateMove(self, move, turn):
		''' 
			Checks to see if the move is an ok move to make on the board 

			Error cases:
			 - There is no piece in the provided point
		 	 - The initial point contains the opposite players pieces
		 	 - The destination point contains two or more of the opposite players pieces
			 > Given the piece is in the first quadrant:
			 	> Given the user is trying to remove the piece:
			 		- There are pieces outside of this quadrant
			 		- The value of the move is greater than the point position 
			 		   AND the point is not the outermost point from the bank
		'''

		direction = turn.getDirection()
		player = turn.getTurn()

		initialPoint = self.board[move[0]]

		if direction == 'anti':
			destinationPoint = self.board[move[0] - move[1]]
		else: 
			destinationPoint = self.board[move[0] + move[1]]

		# initialPieces = 


		return True