#   _____                    _ 
#  /  __ \                  (_)
#  | /  \/ ___ _ __ ___  ___ _ 
#  | |    / _ \ '__/ __|/ _ \ |
#  | \__/\  __/ |  \__ \  __/ |
#   \____/\___|_|  |___/\___|_|
#                              
#  © 2023 Trevor Murphy                            

# Import required modules
import itertools
import random
import time
from values import card_names, card_values, suit_equivalence

# Variable Defaults
global deckOne, deckTwo, handOne, handTwo, deck, end_game, diamond_12_count, playerOne
logDate = 0
deckOne = []
deckTwo = []
handOne = []
handTwo = []
deck = []
diamond_12_count = 0

# Logging Initialization
log = open("log.txt", "w")
debug = open("debug.txt", "w")
logDate = time.ctime()
logTimer = time.time()
log.write("Log generated at " + str(logDate) + ".\nCersei Simulator V. 1.2.5\n© 2023 Trevor Murphy\n\n\n")

def setup():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo, deck

	# Create a deck of cards
	deck = list(itertools.product(range(1, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
	deck.remove((12, 'Heart'))
	deck.remove((12, 'Spade'))
	deck.remove((12, 'Club'))		# Removes/Adds cards to deck to make it in-sync with Cersei rules.
	deck.remove((14, 'Heart'))
	deck.remove((14, 'Spade'))
	random.shuffle(deck)			# Shuffles deck.

	# Divide the deck into two player decks
	deckOne = deck[:26]
	deckTwo = deck[26:]

	# Logs both beginning decks
	log.write("Beginning Decks:		\n\nPlayer 1: " + str(deckOne) + "\n---\nPlayer 2: " + str(deckTwo))

	# Begins game
	log.write("\n\n\nRound #" + str(repeats + 1) + "\n")
	draw(1,True,True)

def draw(number, playerOne, playerTwo):
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo, deck, diamond_12_count
	log.write("\n---------- Drawing Cards ----------\n")

	# Draw "number" amount of cards into player hand
	for _ in range(number):
		if playerOne == True and deckOne:
			drawnCard = deckOne.pop(0)
			handOne.append(drawnCard)
			log.write("Card drawn (Player One): " + str(drawnCard) + "\n")
		if playerTwo == True and deckTwo:
			drawnCard = deckTwo.pop(0)
			handTwo.append(drawnCard)
			log.write("Card drawn (Player Two): " + str(drawnCard) + "\n")
	else:
		None

	calculateModifiers()

def draw2(number, playerOne, playerTwo):
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo, deck, diamond_12_count
	log.write("\n---------- Drawing Cards ----------\n")

	# Draw "number" amount of cards into player hand
	if deckOne and deckTwo:	
		for _ in range(number):
			if playerOne == True and deckOne:
				drawnCard = deckOne.pop(0)
				handOne.append(drawnCard)
				log.write("Card drawn (Player One): " + str(drawnCard) + "\n")
			if playerTwo == True and deckTwo:
				drawnCard = deckTwo.pop(0)
				handTwo.append(drawnCard)
				log.write("Card drawn (Player Two): " + str(drawnCard) + "\n")
	else:
		calculateWinner()
	calculateModifiers()

def cardValues():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo
	log.write("\n---------- Card Value Calculation ----------\n")

	# Recalculate top card value
	if handOne != 1:
		log.write("Player 1 Hand: " + str(handOne) + "\n")
		old_card_value = handOne[-1][0]
		suit = handOne[-1][1]
		new_card_value = card_values.get(old_card_value, old_card_value)
		handOne[-1] = (old_card_value, suit, new_card_value)  # Replace the tuple with the new one
		log.write("Player 1 Adjusted Hand: " + str(handOne) + "\n")
	# Check for recalculated value cards:
	elif handOne[-1][0] == 1:
		new_card_value = cannon_value(handTwo[-1][1], handOne[-1][1])
		log.write("Player 1 Hand: " + str(handOne) + "\n")
		old_card_value = handOne[-1][0]
		suit = handOne[-1][1]
		handOne[-1] = (old_card_value, suit, new_card_value)  # Replace the tuple with the new one
		log.write("Player 1 Adjusted Hand: " + str(handOne) + "\n")
		debug.write("round " + str(repeats + 1) + "\n " + str(handOne))

	# Check Hand 2
	if handTwo != 1:
		log.write("Player 2 Hand: " + str(handTwo) + "\n")
		old_card_value = handTwo[-1][0]
		suit = handTwo[-1][1]
		new_card_value = card_values.get(old_card_value, old_card_value)
		handTwo[-1] = (old_card_value, suit, new_card_value)  # Replace the tuple with the new one
		log.write("Player 2 Adjusted Hand: " + str(handTwo) + "\n")
	# Check for recalculated value cards:
	elif handTwo[-1][0] == 1:
		new_card_value = cannon_value(handOne[-1][1], handTwo[-1][1])
		log.write("Player 2 Hand: " + str(handTwo) + "\n")
		old_card_value = handTwo[-1][0]
		suit = handTwo[-1][1]
		handTwo[-1] = (old_card_value, suit, new_card_value)  # Replace the tuple with the new one
		log.write("Player 2 Adjusted Hand: " + str(handTwo) + "\n")

	
	checkWars()

def cannon_value(opponentSuit, aceSuit):
	opponentValid = int(suit_equivalence.get(opponentSuit, opponentSuit))
	aceValid = int(suit_equivalence.get(aceSuit, aceSuit))
	#print(opponentValid, aceValid)
	if opponentValid != aceValid:
		return -14
	else:
		return 14

def calculateModifiers():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo
	log.write("\n---------- Calculate Modifiers ----------\n")

	# Check for 5 cards in hand.
	if handOne[-1][0] == 5:
		log.write("Modifiers applied to player 1! Drawing.\n")
		draw2(1,True,False)
		newCard = (handOne[-1][0], handOne[-1][1], handOne[-1][0] + handOne[-2][0])
		handOne.append(newCard)
		handOne.pop(-1)
		#print("5 Drawn")
		log.write("New player 1 card value with modifications: " + str(newCard[0]) + "\n")
	elif handOne[-1][0] == 8:
		log.write("Modifiers applied to player 1! Drawing.\n")
		draw2(1,True,False)
		newCard = (handTwo[-1][0], handTwo[-1][1], handTwo[-1][0] - handOne[-1][0])
		handTwo.append(newCard)
		handOne.pop(-1)
		#print("8 Drawn")
		log.write("New player 2 card value with modifications: " + str(newCard[0]) + "\n")
	if handTwo[-1][0] == 5:
		log.write("Modifiers applied to player 2! Drawing.\n")
		draw2(1,False,True)
		newCard = (handTwo[-1][0], handTwo[-1][1], handTwo[-1][0] + handTwo[-2][0])
		handTwo.append(newCard)
		handTwo.pop(-1)
		#print("5 Drawn")
		log.write("New player 2 card value with modifications: " + str(newCard[0]) + "\n")
	elif handTwo[-1][0] == 8:
		log.write("Modifiers applied to player 2! Drawing.\n")
		draw2(1,False,True)
		newCard = (handOne[-1][0], handOne[-1][1], handOne[-1][0] - handTwo[-1][0])
		handOne.append(newCard)
		handTwo.pop(-1)
		#print("8 Drawn")
		log.write("New player 1 card value with modifications: " + str(newCard[0]) + "\n")

	checkBattles()

def checkBattles():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo
	log.write("\n---------- Check for Battles ----------\n")

	if handOne[-1][0] == 2 or handTwo[-1][0] == 2:
		log.write("Battle found! Drawing.\n")
		draw2(2,True,True)
		cardValues()
	else:
		log.write("No battles found.\n")
		cardValues()

def checkWars():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo, player1, diamond_12_count
	log.write("\n---------- Check for Wars ----------\n")

	# Check for wars
	if handOne[-1][2] == handTwo[-1][2]:
		log.write("War found! Drawing.\n")
		draw2(3,True,True)
		cardValues()
	else:
		log.write("No wars found.\n")
		calculateWinner()

def calculateWinner():
	# Declare global variables
	global deckOne, deckTwo, handOne, handTwo, diamond_12_count
	log.write("\n---------- Calculate Winner ----------\n")

	#print(handOne)

	# Check for queen of diamonds:
	if handOne and handOne[-1][0] == 12 and handOne[-1][1] == 'Diamond':
		diamond_12_count += 1
	elif handTwo and handTwo[-1][0] == 12 and handTwo[-1][1] == 'Diamond':
		diamond_12_count += 1

	if handOne[-1][2] > handTwo[-1][2]:
		log.write("Player 1 wins round " + str(repeats + 1) + "\n")
		deckOne.extend(handOne + handTwo)
	else:
		log.write("Player 2 wins round " + str(repeats + 1) + "\n")
		deckTwo.extend(handTwo + handOne)

	endOfTurnAbilities(handOne, handTwo)

def endOfTurnAbilities(handOne, handTwo):
	# Declare global variables
	global deckOne, deckTwo, diamond_12_count
	log.write("\n---------- End of Turn Abilities ----------\n")

	if handOne[-1][0] == 15 or handOne[0][0] == 15 or handTwo[-1][0] == 15 or handTwo[0][0] == 15:
		random.shuffle(handOne)
		random.shuffle(handTwo)
		if (12, 'Diamond') in deckOne:
			deckOne.remove((12, 'Diamond'))
			deckOne.append((12, 'Diamond'))
		if (12, 'Diamond') in deckTwo:
			deckTwo.remove((12, 'Diamond'))
			deckTwo.append((12, 'Diamond'))

	# Clear both players' hand	
	handOne.clear()
	handTwo.clear()

	endTurn()

def endTurn():
	# Writes decks to logs
	log.write("Final decks after round:\nPlayer 1:   " + str(deckOne) + "\nPlayer 2:   " + str(deckTwo) + "\n")
	debug.write("# of cards: " + str(len(deckOne) + len(deckTwo)) + "\n")

	# Checks for 12 of diamonds 3 times
	if diamond_12_count >= 3:
		endGame()
	elif len(deckOne) == 0 or len(deckTwo) == 0:
		endGame()

def endGame():
	# Declare global variables
	global end_game
	# End the game.
	end_game = True

	# Check scores
	if len(deckOne) > len(deckTwo):
		print("\n\n--------------------\nPlayer 1 Wins!")
		log.write("\n\n--------------------\nPlayer 1 Wins!")
	else:
		print("\n\n--------------------\nPlayer 2 Wins!")
		log.write("\n\n--------------------\nPlayer 2 Wins!")

	log.write("\nLog generated at: " + str(logDate) + "\nCompleted in " + str(time.time() - logTimer) + " seconds.")

## Game Loop

# Initialize game variables
repeats = 0
end_game = False
setup()

# Main loop for the game
while not end_game:
	round(repeats)
	repeats += 1
	round(diamond_12_count)
	print("Queen Value: ", diamond_12_count)
	log.write("\n\n\nRound #" + str(repeats + 1) + "\n")
	draw(1,True,True)

# Print the end of the game
print("\n\nGame ended after", repeats, "rounds.")
