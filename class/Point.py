class Point:
	position = 0

	def __init__(self, pos):
		self.position = pos
		self.pieces = []

	def getPosition(self):
		return self.position

	def getPieces(self):
		return self.pieces

	def addPiece(self, pc):
		self.pieces.append(pc)

	def popPiece(self):
		self.pieces.pop()

	def getLenPieces(self):
		return len(self.pieces)