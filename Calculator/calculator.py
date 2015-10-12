st1 = int(raw_input("Vnesi stevilo:"))
st2 = int(raw_input("Vnesi stevilo:"))

operator = raw_input("Operator?")

if operator == "+" or operator == "plus":
	sest = st1 + st2
	print sest
elif operator == "-" or operator == "minus":
	odst = st1 - st2
	print odst
elif operator == "*" or operator == "krat" or operator == "mnozenje":
	mnoz = st1 * st2
	print mnoz
elif opeartor == "/" or operator == "deljenje":
	delj = st1 / st2
	print delj

