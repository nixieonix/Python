
seznam = {
	"mleko": 2.25,
	"kruh": 1.22,
	"jajca": 2.5,
	"paprika": 3.1
}

nakupovanje = True
vsota = 0
maxVrednostNakupa = 5
seznamIzdelkov = []
while nakupovanje:
	#prodajalka nas prasa kaj bomo kupili
	izdelek = raw_input("Kaj nakupujemo?")

	if izdelek in seznam.keys():
		seznamIzdelkov.append(izdelek)
		cenaIzdelka = seznam[izdelek]
		
		#if izdelek == "konec" or vsota >= maxVrednostNakupa:
		#	nakupovanje = False
		if vsota + cenaIzdelka > maxVrednostNakupa:
			print "Presegel bi nakup"
		else:
			print "cena izdelka je: ", cenaIzdelka
			vsota = vsota + cenaIzdelka

	elif izdelek == "konec":
		print "Kupili smo: "
		for j in seznamIzdelkov:
			print j
		print "Vrednost nakupa: ", vsota
		break	
	else:
		print "Izdelka ni na seznamu!"





# TODO preveri ali je izdelek v seznamu,
# ce je  sestej vrednost nakupovanje
#
# ce je izdelek enak konec, porgram prekini
# izpisi vsoto nakupa