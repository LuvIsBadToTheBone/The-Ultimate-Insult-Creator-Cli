import random
#u need python3-pyperclip cross-platform Python3 module for copy and paste from/to clipboard.
#Beleidigungen für Frauen
import pyperclip as pc

collumn1 = ["FAULE","BLÖDE","IDIOTISCHE","SCHLEIMIGE","STINKENDE","RASSISTISCHE","ELITÄRE","DROGENABHÄNGIGE","ARSCHGESICHTIGE","GESCHMACKSVERIRRTE","HÄSSLCHE","WIDERWÄRTIGE","VERFICKTE","ELENDE","BORNIERTE","EINFÄLTIGE","KLEINKARIERTE","LANGWEILIGE","SCHEINHEILIGE","SOZIOPATHISCHE","STURE"]
collumn2 = ["ARSCH","REKTUM","FOTZEN","SCHLAMPIGE","FICK","FEUCHTE","FROSCHIGE","HOHLKÖPFIGE","TOLLPATSCHIGE","BEPISSTE","GESTÖRTE","EIERKÖPFIGE","UNTALENTIERTE","BEHAARTE","NOTGEILE","CHARAKTERLOSE","INKOMPETENTE","FEIGE","RÄUDIGE","UNFÖRMIGE","PERVERSE"]
collumn3 = ["GEHIRNAMPUTIERTE","KUH","DIVA","HURE","SCHLUCKSCHLAMPE","SCHABRACKE","SCHLAMPE","FREGATTE","GEWITTERHEXE","SCHNEPFE","HEXE","PUTE","EMANZE","SPERMATOILETTE","SCHLANGE","FOTZE","MISSGEBURT","KACKBRATZE","FURZREIBE","PISSNASE","DUMMBRATZE"]

num1len = (len(collumn1))
num2len = (len(collumn2))
num3len = (len(collumn3))

pick1 = random.randint(0,num1len-1)
pick2 = random.randint(0,num2len-1)
pick3 = random.randint(0,num3len-1)

insult = collumn1[pick1] + " " + collumn2[pick2] + " " + collumn3[pick3]
pc.copy(insult)
print(insult, "wurde in die Zwischenablage kopiert..")
