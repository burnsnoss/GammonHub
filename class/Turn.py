class Turn:
	''' 
		The Turn class keeps track of whose turn it is, the direction play is going in,
		 the rolls that remain, and the moves made the current turn.
	'''
	rolls = []
	movesMade = []
	turn = ''
	turnPrint = ''
	turnCount = 0
	direction = ''

	def __init__(self, starter, homeColor):

		# Set turn and dir variables 
		self.turn = starter
		self.setTurnPrint()
		if homeColor == 'b':
			if starter == 'b':
				self.direction = 'anti'
			else:
				self.direction = 'clock'
		else:
			if starter == 'b':
				self.direction = 'clock'
			else: 
				self.direction = 'anti'

	def setTurnPrint(self):
		if self.turn == 'b':
			self.turnPrint = 'Black'
		else:
			self.turnPrint = 'White'
		return self.turnPrint

	def getTurnPrint(self):
		return self.turnPrint

	def getTurn(self):
		return self.turn

	def setRolls(self, newRolls):
		self.movesMade = []
		self.rolls = newRolls
		return

	def appendRoll(self, roll):
		self.rolls.append(roll)
		return

	def removeRoll(self, roll):
		self.rolls.remove(roll)
		return

	def printRoll(self):
		msg = ''
		for roll in self.rolls:
			msg += str(roll) + ' '
		return msg

	def getDirection(self):
		return self.direction 

	def nextTurn(self):
		if self.turn == 'b':
			self.turn = 'w'
		else:
			self.turn = 'b'

		if self.direction == 'anti':
			self.direction = 'clock'
		else:
			self.direction = 'anti'

		self.setTurnPrint()

		return self.turn