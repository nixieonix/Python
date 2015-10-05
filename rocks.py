# -*- coding: utf-8 -*-
import random

rock = random.randint(4, 20)
move = 0
print "Na zacetku je na kupu " + str(rock) + " kamenckov."
print "Lahko vzames samo enega, dva ali tri kamencke!"

while rock > 0:
	if move % 2 == 0:
		if rock != 0:
			while True:
				num1 = int(raw_input("Na potezi je igralec 1: "))
				if num1 == 1 or num1 == 2 or num1 == 3:
					break
			if rock < num1:
				print "Ne mores vzeti vec kamnov kot jih je na kupu..."
			else:
				rock = rock - num1
				print "Potezo je naredil igralec 1. Na kupu je se " + str(rock) + " kamenckov!"
				move = move + 1	
	
	elif move % 2 != 0:
		if rock != 0:
			while True:
				num2 = int(raw_input("Na potezi je igralec 2: "))
				if num2 == 1 or num2 == 2 or num2 == 3:
					break

			if rock < num2:
				print "Ne mores vzeti vec kamnov kot jih je na kupu..."
			else:
				rock = rock - num2
				print "Potezo je naredil igralec 2. Na kupu je se " + str(rock) + " kamenckov!"
				move = move + 1
		
if rock == 0 and move % 2 != 0:
	print "Igralec 1 je izgubil igro!"
else:
	print "Igralec 2 je izgubil igro!"
			


