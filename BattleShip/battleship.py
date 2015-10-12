
from random import randint

boatField = []

for i in range(0, 5):
	boatField.append(["0"] * 5)

def print_board(boatField):
	for row in boatField:
		print " ".join(row)

random_row = randint(0, len(boatField) - 1)
random_col = randint(0, len(boatField[0]) - 1)

print "Let's play battle ship!"
print print_board(boatField)

for turn in range(4):
	guess_row = int(raw_input("Guess Row: "))
	guess_col = int (raw_input("Guess Col: "))

	if random_row == guess_row and random_col == guess_col:
		print "You sank my battleship!"
		break
	else:
		if guess_row not in range(5) or guess_col not in range(5):
			print "Oops, that's not even in the ocean."

		elif boatField[guess_row][guess_col] == "X":
			print "You already tried this one!"

		else:
			print "You missed my battleship!"
			boatField[guess_row][guess_col] = "X"
	
	print "Turn: ", turn + 1
	print_board(boatField)
	
	if turn == 3:
		print "Game Over"
		print random_row
		print random_col

"""
from random import randint

boatField = []

# Pick number one between 0 and 50, then pick
# number 2 between the first picked number and
# 100. Make sure that the ship size is at least
# 5 and not bigger than 8. 
# If not, repeat the procedure until you get
# two "good numbers"

shipStartField = randint(0, 30)
shipEndField = randint(shipStartField, 30)

print "Ship is between %d and %d" % (shipStartField, shipEndField)

# Set the boat in the boat list
for i in range(shipStartField, shipEndField + 1):
	boatField[i] = True

gameRunning = True
shipPiecesLeft = 0

while gameRunning:
	# What to add?
	# target = raw_input - prompt player to pick a 
	# number between 0 and 30, make sure that the
	# input is integer (number) before using it

	# BONUS: Check if the user picked the right
	# number (between 0 and 30, if he hasn't, 
	# prompt him for the number again)

	# TODO: Uncomment this line and read user input ...
	#target = 

	if boatField[target] == True:
		print "Boat hit!"
		# TODO: Set the target in boat field to False
	else:
		print "Missed!"
	
	# Check if we still have any ship pieces left
	# (was the boat sunk)
	for i in range(0, 30):
		if boatField[i] == True:
			shipPiecesLeft = shipPiecesLeft + 1
	if shipPiecesLeft == 0:
		gameRunning = False
	else:
		shipPiecesLeft = 0

print "You sank my battleship!"
"""




