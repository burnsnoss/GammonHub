class Piece:
	color = ''

	def __init__(self, c):
		self.color = c

	def getColor(self):
		return self.color

	def printPiece(self):
		if self.color == 'w':
			return 'O'
		else:
			return '0'

	# def changePiece(self, newChar, color):
	# 	if color == 'b':
	# 		self.b_printPiece = newChar
	# 	else:
	# 		self.w_printPiece = newChar

	# 	return
