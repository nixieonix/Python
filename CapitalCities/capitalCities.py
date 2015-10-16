# -*- coding: utf-8 -*-
import random

states ={
	"Slovenia" : "Ljubljana",
	"Croatia": "Zagreb",
	"Iceland" : "Reykjavík",
	"Australia": "Canberra",
	"China": "Beijing",
	"Japan": "Tokyo",
	"USA": "Washington",
	"Canada": "Ottawa",
	"England": "London",
	"Ireland": "Dublin"
} 

game = True
scores = 0

while game:
	key = random.choice(states.keys())
	print "What is the capital city of %s? " % (key) 
	city = raw_input("Answer: ")

	if city == states[key]:
		print "OK"
		scores = scores + 1
	elif city == "konec":
		game = False
		break
	elif city != states[key]:
		print "Not OK!"
	

print "Youre scores: ", scores