from random import randint


player1 = []
dice1 = randint(1,6)
player1.append(dice1)
player2 = []
dice2 = randint(1,6)
player2.append(dice2)

print "Player 1: " + str(player1[0])
print "Player 2: " + str(player2[0])

if player1 < player2:
	print "Player 2 wins!"
elif player1 > player2:
	print "Player 1 wins!"
elif player1 == player2:
	print "Match Draw!"


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