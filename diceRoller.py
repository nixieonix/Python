from random import randint


player1 = []
dice1 = randint(1,6)
player1.append(dice1)
player2 = []
dice2 = randint(1,6)
player2.append(dice2)



ply1score = 20
ply2score = 20

while ply1score > 0 or ply2score > 0:
	if ply1score != 0 and ply2score != 0:
		dice1 = randint(1,6)
		dice2 = randint(1,6)
		
		if ply1score < dice1 or ply2score < dice2:
			print "Player 1: " + str(dice1)
			print "Player 2: " + str(dice2)
		else:
			ply1score = ply1score - dice1
			ply2score = ply2score - dice2

		print "Player 1: " + str(dice1) + " Score: " + str(ply1score)
		print "Player 2: " + str(dice2) + " Score: " + str(ply2score)


	else: 
		if ply1score == 0 and ply2score != 0:
			print "Igra je koncana, zmagal je igralec 1!"
			break
		elif ply2score == 0 and ply1score != 0:
			print "Igra je koncana, zmagal je igralec 2!"
			break
		else:
			print "Igra je nedolocena!"
			break





"""if player1 < player2:
	print "Player 2 wins!"
elif player1 > player2:
	print "Player 1 wins!"
elif player1 == player2:
	print "Match Draw!"
"""


"""question = raw_input("Are you ready? ")

if question == "yes":
	diceNumb = int(raw_input("How many dice do you need?"))
	i = 0
	while diceNumb > i:
		dice = randint(1,6)
		print dice
		i = i + 1
elif question == "no": 
	print ("OK: Come agein latter!")"""



"""if question == "yes" or question == "y":
	dice = randint(1,6)
	print dice
elif question == "no" or question == "n":
	print("OK! Next time!")"""