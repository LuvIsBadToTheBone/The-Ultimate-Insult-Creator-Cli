import random

collumn1 = ["LAZY","STUPID","INSECURE","IDOTIC","SLIMY","SLUTTY","SMELLY","POMPOUS","COMMUNIST","DICKNOSE","PIE-EATING","RACIST","ELITIST","WHITE TRASH","DRUG-LOVING","BUTTERFACE","TONE DEAF","UGLY","CREEPY"]
collumn2 = ["DOUCHE","ASS","TURD","RECTUM","BUTT","COCK","SHIT","CROTCH","BITCH","TURD","PRICK","SLUT","TAINT","FUCK","DICK","BONER","SHART","NUT","SPHINTER"]
collumn3 = ["PILOT","CANOE","CAPTAIN","PIRATE","HAMMER","KNOB","BOX","JOCKEY","NAZI","WAFFLE","GOBLIN","BLOSSOM","BISCUIT","CLOWN","SOCKET","MONSTER","HOUND","DRAGON","BALLOON"]

num1len = (len(collumn1))
num2len = (len(collumn2))
num3len = (len(collumn3))

pick1 = random.randint(0,num1len-1)
pick2 = random.randint(0,num2len-1)
pick3 = random.randint(0,num3len-1)

print(collumn1[pick1], collumn2[pick2], collumn3[pick3])
