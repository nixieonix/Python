# -*- coding: utf-8 -*-

code = open("dna.txt", "r").read()
#code = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

print "Nas kodni zapis vsebuje " + str(code.count("C")) + " citozinov!"
print "Nas kodni zapis vsebuje " + str(code.count("A")) + " adeninnov!"
print "Nas kodni zapis vsebuje " + str(code.count("T")) + " timinov!"
print "Nas kodni zapis vsebuje " + str(code.count("G")) + " gvaninov!"

print "Opis osumljenca:"

hair = {"hairBlack": "CCAGCAATCGC","hairBrown": "GCCAGTGCCG", "hairGinger": "TTAGCTATCGC"}
if code.find(hair["hairBlack"]) != -1:
	las = "black"
	print "Lasje: crni"
elif code.find(hair["hairBrown"]) != -1:
	las = "brown"
	print "Lasje: rjavi"
elif code.find(hair["hairGinger"]) != -1:
	las = "ginger"
	print "Lasje: korencek"

face = {"square": "GCCACGG", "circle": "ACCACAA", "oval": "AGGCCTCA" }
if code.find(face["square"]) != -1:
	obraz = "square"
	print "Obraz: kvadraten"
elif code.find(face["circle"]) != -1:
	obraz = "circle"
	print "Obraz: okrogel"
elif code.find(face["oval"]) != -1:
	obraz = "oval"
	print "Obraz: ovalen"

eyes = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
if code.find(eyes["blue"]) != -1:
	oci = "blue"
	print "Oci: modre"
elif code.find(eyes["green"]) != -1:
	oci = "green"
	print "Oci: zelene"
elif code.find(eyes["brown"]) != -1:
	oci = "brown"
	print "Oci: rjave"

sex = {"male": "TGCAGGAACTTC", "female": "TGAAGGACCTTC"}
if code.find(sex["male"]) != -1:
	spol = "male"
	print "Spol: moski"
elif code.find(sex["female"]) != -1:
	spol = "female"
	print "Spol: zenski "

race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
if code.find(race["white"]) != -1:
	print "Rasa: bela"
elif code.find(race["black"]) != -1:
	print "Rasa: crna"
elif code.find(race["asian"]) != -1:
	print "Rasa: rumena"

ziga = {"sex": "male", "race": "white", "hair": "ginger", "eyes": "brown", "face": "circle"}
if ziga["sex"] == spol and ziga["hair"] == las and ziga["eyes"] == oci and ziga["face"] == obraz:
	print "Nas osumljenec je Ziga!"
matej = {"sex": "male", "race": "white", "hair": "black", "eyes": "blue", "face": "oval"}
if matej["sex"] == spol and matej["hair"] == las and matej["eyes"] == oci and matej["face"] == obraz:
	print "Nas osumljenec je Matej!"
miha = {"sex": "male", "race": "white", "hair": "brown", "eyes": "green", "face": "square"}
if miha["sex"] == spol and miha["hair"] == las and miha["eyes"] == oci and miha["face"] == obraz:
	print "Nas osumljenec je Miha!"

"""
#barva las
crna = "CCAGCAATCGC"
rjava = "GCCAGTGCCG"
korencek = "TTAGCTATCGC"

las1 = code.find(crna)
las2 = code.find(rjava)
las3 = code.find(korencek)

if las1 != -1:
	print "Lasje: crni"
elif las2 != -1:
	print "Lasje: rjavi"
elif las3 != -1:
	print "Lasje: korencek"

# oblika obrza
kvadraten = "GCCACGG"
okrogel = "ACCACAA"
ovalen = "AGGCCTCA"

obr1 = code.find(kvadraten)
obr2 = code.find(okrogel)
obr3 = code.find(ovalen)

if obr1 != -1:
	print "Obraz: kvadraten"
elif obr2 != -1:
	print "Obraz: okrogel"
elif obr3 != -1:
	print "Obraz: ovalen"

#barva oci
modra = "TTGTGGTGGC"
zelena = "GGGAGGTGGC"
rjavaOci = "AAGTAGTGAC"

oci1 = code.find(modra)
oci2 = code.find(zelena)
oci3 = code.find(rjavaOci)

if oci1 != -1:
	print "Oci: modre"
elif oci2 != -1:
	print "Oci: zelene"
elif oci3 != -1:
	print "Oci: rjave"

#rasa
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

rasa1 = code.find(belec)
rasa2 = code.find(crnec)
rasa3 = code.find(azijec)

if rasa1 != -1:
	print "Rasa: bela"
elif rasa2 != -1:
	print "Rasa: crna"
elif rasa3 != -1:
	print "Rasa: rumena"
"""