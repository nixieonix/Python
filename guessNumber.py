import random

player1 = []
player1.append(random.randint(0,10))
player2 = []
player2.append(random.randint(0,10))
i = 0

print int(player1[0])
print int(player2[0])

while i < 10:
	playerGuess1 = int(raw_input("Igralec 1 vnesi st:"))
	playerGuess2 = int(raw_input("Igralec 2 vnesi st:"))
	
	if int(player1[0]) == playerGuess1 and int(player2[0]) != playerGuess2:
		print "Player 1 wins!"
		break
	elif int(player2[0]) == playerGuess2 and int(player1[0]) != playerGuess1:
		print "Player 2 wins!"
		break
	elif int(player1[0]) == playerGuess1 and int(player2[0]) == playerGuess2:
		print "Match Draw!"
		break
	elif i == 9 and int(player1[0]) != playerGuess1 and int(player2[0]) != playerGuess2:
		print "Game Over!"
		break
	else:
		print "Try again!"
		i = i + 1



"""
guessNumber = randint(0,10)
i = 0

print guessNumber

while(i < 10):
	guess = int(raw_input("Vnesi st:"))
	if(guess== guessNumber):
		print("OK!")
		break
	elif (i == 9 and guess != guessNumber):
		print("You lose!")
		break
	else:
		print("Try agin!")
		i = i + 1
"""