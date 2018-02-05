def printWelcome():
	print " "
	print "   - W E L C O M E   T O   B A C K G A M M O N - "
	print " "

def getGameType():
	print " "
	print "        - S E L E C T   G A M E   T Y P E - "
	print " "
	print "              1 - O N E   P L A Y E R  "
	print "             2 - T W O   P L A Y E R S "
	print " "
	print "   T Y P E   quit   A N Y T I M E   T O   E X I T "
	print " "

	while True:
		game_type = raw_input("             G A M E   T Y P E ? --> ")

		if game_type == "1":
			return 1
		elif game_type == "2":
			return 2
		elif game_type == "quit":
			exit()
		else:
			print " "
			print "     - P L E A S E   I N P U T   1   O R   2 - "
			print " "
			print "              1 - O N E   P L A Y E R  "
			print "             2 - T W O   P L A Y E R S "
			print " "
			print "   T Y P E   quit   A N Y T I M E   T O   E X I T "
			print " "

def getColor():
	print " "
	print "    - S E L E C T   P L A Y E R 1   C O L O R - "
	print " "
	print "                 b  -  B L A C K "
	print "                 w  -  W H I T E "
	print " "

	while True:
		color = raw_input("                C O L O R ? --> ")

		if color == 'b' or color == 'w':
			return color
		elif color == 'quit':
			exit()
		else:
			print " "
			print "     - P L E A S E   I N P U T   b   O R   w - "
			print " "

def logError(errorType, msg):
	pass # if 