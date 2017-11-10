import random

class Dice:
	'''
		Not too sure if this class will be anything more than a dice roller. It
		 turns a doubles roll into four 'rolls' upon roll, also determines starter
	'''
	rolls = []

	def roll(self):
		# Trusty dice roller
		# Reset rolls list
		self.rolls = []

		# Get dice values
		first, second = self.generateNumbers()

		if first == second:
			# Doubles, add four numbers to list
			for i in range(4):
				self.rolls.append(first)
		elif first > second:
			# Append larger roll first
			self.rolls.append(first)
			self.rolls.append(second)
		else:
			self.rolls.append(second)
			self.rolls.append(first)

		return self.rolls

	def generateNumbers(self):
		first = random.randint(1,6)
		second = random.randint(1,6)
		return first, second

	def determineStarter(self):
		# Simple function to determine who starts
		# Rolls two dice, returns 1 or 2 based on 
		#  which one is the larger roll
		while True:
			first, second = self.generateNumbers()
			print 
			if first > second:
				return 1
			elif second > first:
				return 2