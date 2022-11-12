import random
#u need python3-pyperclip cross-platform Python3 module for copy and paste from/to clipboard.
#Beleidigt zufällig auf deutsch, für Männer.
import pyperclip as pc

collumn1 = ["FAULER","BLÖDER","IDIOTISCHER","SCHLEIMIGER","STINKENDER","RASSISTISCHER","ELITÄRER","DROGENABHÄNGIGER","ARSCHGESICHTIGER","GESCHMACKSVERIRRTER","HÄSSLCHER","WIDERWÄRTIGER","VERFICKTER","ELENDER","BORNIERTER","EINFÄLTIGER","KLEINKARIERTER","LANGWEILIGER","SCHEINHEILIGER","SOZIOPATHISCHER","STURER"]
collumn2 = ["ARSCH","REKTUM","SCHWANZ","SCHLAMPIGER","FICK","ERRIGIERTER","FROSCH","HOHLKÖPFIGER","TOLLPATSCHIGER","BEPISSTER","GESTÖRTER","EIERKÖPFIGER","UNTALENTIERTER","BEHAARTER","NOTGEILER","CHARAKTERLOSER","INKOMPETENTER","FEIGER","RÄUDIGER","UNFÖRMIGER","PERVERSER"]
collumn3 = ["PILOT","KAPITÄN","NAZI","CLOWN","TROTTEL","AFFE","KARAMELRINGLIEBHABER","GEHIRNAMPUTIERTER","HURENSOHN","VOLLIDIOT","LUSTMOLCH","DUMMSCHWÄTZER","KNALLKOPP","ESEL","TERRORIST","LUTSCHER","PLAYBOY","PASCHA","TAUGENICHTS","SCHWANZ","GAUNER"]

num1len = (len(collumn1))
num2len = (len(collumn2))
num3len = (len(collumn3))

pick1 = random.randint(0,num1len-1)
pick2 = random.randint(0,num2len-1)
pick3 = random.randint(0,num3len-1)

insult = collumn1[pick1] + " " + collumn2[pick2] + " " + collumn3[pick3]
pc.copy(insult)
print(insult, "wurde in die Zwischenablage kopiert..")
