from random import randint


player1 = raw_input("Your move! ")
player2 = ["rock", "paper", "scissors"]

player2 = player2[randint(0,2)]

print "Player 1 chooses: " + player1
print "Player 2 chooses: " + player2

if player1 == "rock":
	if player2 == "rock":
		print "Match Draw!"
	elif player2 == "paper":
		print "Player 2 wins!"
	elif player2 == "scissors":
		print "Player 1 wins!"
elif player1 == "paper":
	if player2 == "rock":
		print "Player 1 wins!"
	elif player2 == "paper":
		print "Match Draw!"
	elif player2 == "scissors":
		print "Player 2 wins!"
elif player1 == "scissors":
	if player2 == "rock":
		print "Player 2 wins!"
	elif player2 == "paper":
		print "Player 1 wins!"
	elif player2 == "scissors":
		print "Match Draw!"