#Hrvatske uvrede.(croatian insults) 

#Contributor: Obi-Van-Konobe

#u need python3-pyperclip cross-platform Python3 module for copy and paste from/to clipboard.

import random
import pyperclip as pc

collumn1 = ["SMRDLJIVI","UŠLJIVI","ODVRATNI","OGAVNI","PRLJAVI","BLESAVI","RETARDIRANI","ZAOSTALI","NEDOJEBANI","JEFTINI","RUŽNI","POKVARENI","POREMEĆENI","GLUPI","MONGOLOIDNI"]
collumn2 = ["USRANI", "NEOPRANI", "PREPOTENTNI", "NARCISOIDNI", "GUZIČARSKI", "NASTRANI", "ZAJEBANI", "TUPAVI", "IDIOTSKI", "KURVINSKI", "GOVNARSKI", "IRITANTNI", "DOSADNI", "KRETENSKI", "LUDI"]
collumn3 = ["ŠUPKU", "DEBILU", "LUĐAČE", "IMBECILU", "PEDERU", "KRETENU", "GOVNARU", "SERONJO", "IDIOTE", "MAJMUNE", "KONJU", "ĐUBRETARU", "MAGARČE", "SMETLARU", "GUZOJEBAČU", "IZRODE", "PROLJEVU"]

num1len = (len(collumn1))
num2len = (len(collumn2))
num3len = (len(collumn3))

pick1 = random.randint(0,num1len-1)
pick2 = random.randint(0,num2len-1)
pick3 = random.randint(0,num3len-1)

insult = collumn1[pick1] + " " + collumn2[pick2] + collumn3[pick3]
pc.copy(insult)
print(insult, "kopirano u clipboard.")
