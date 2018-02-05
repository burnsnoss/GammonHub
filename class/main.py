import Board
import Turn
import Dice
import Util
import Move


def validateMove(move):
	pass

def startOnePlayerGame(color):
	board = Board.Board(color)
	board.printBoard()

def startTwoPlayerGame(color):
	board = Board.Board(color)
	dice = Dice.Dice()

	board.printBoard()

	print 'Determining Starter...'
	starter = dice.determineStarter()

	if starter == 1:
		turn = Turn.Turn(color, color) 
	else:
		if color == 'b':
			turn = Turn.Turn('w', color)
		else:
			turn = Turn.Turn('b', color)

	while True:
		print turn.getTurnPrint() + "'s turn."
		print turn.getTurnPrint() + "'s roll:"

		turn.setRolls(dice.roll())
		print turn.printRoll()

		# Get and validate move from the player
		move = Move.getPlayerMove(turn, board)

		# Make the move
		if move == 'undo':
			board.undoMove(turn)
			turn.undoMove()
		else:
			pass
			

		break

		# move = raw_input('First move? --> ')

		# move = errorCheckUserInput(move)

		# if move == 'quit':
		# 	exit()
		# elif validateUserInput(move)




if __name__ == "__main__":

	Util.printWelcome()

	game_type = Util.getGameType()

	color = Util.getColor()

	if game_type == 1:
		# startOnePlayerGame(color)
		pass
	elif game_type == 2:
		startTwoPlayerGame(color)
	else:
		print " ERROR: CODE 69 "
		print " PLEASE CONTACT YOUR ADMINISTRATOR "
		exit()


exit()
