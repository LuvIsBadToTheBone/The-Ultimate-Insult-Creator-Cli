#Hollandse Beledigingen. Contributor: dramo
#u need python3-pyperclip cross-platform Python3 module for copy and paste from/to clipboard.
import random
import pyperclip as pc

collumn1 = ["LUIE","STOMME","ONZEKERE","KRANKZINNIGE","GLADDERIGE","SLETTERIGE","STINKENDE","OPGEBLAZEN","COMMUNISTISCHE","MARXISTISCHE","LULLIGE","LINKSE","ELITAIRE","SNUIVENDE","ALLESVRETENDE","NOOITTEVREDENE","TOONDODE","LELIJKE","ENGE","VERACHTELIJKE","VIEZE","VUILE","LEUGENACHTIGE","RANZIGE","PARASITERENDE","MANIPULERENDE","VERRADERLIJKE"]
collumn2 = ["KANKER","KENKER","KUT","TYFUS","SCHIJT","POEP","TERING","PEST","ZWAM","ZWENDEL","ZAKKEN","ONGELUKS","MONGOLEN","JAT","PILLEN"]
collumn3 = ["OVERLOPER","LUL","LULHANNES","WASSER","VOLKSMENNER","JOOD","VERSPREIDER","WIJF","NEUS","EIKEL","TEEF","LIJAARD","KNEUS","KOP","DOOS","RAKKER","SUKKEL","CLOWN","PIJPERD","SPOOK","ZAK","LIKKER","DIKZAK","SCHIJTERD","VEELVRAAT","KOEKWAUS"]

num1len = (len(collumn1))
num2len = (len(collumn2))
num3len = (len(collumn3))

pick1 = random.randint(0,num1len-1)
pick2 = random.randint(0,num2len-1)
pick3 = random.randint(0,num3len-1)

insult = collumn1[pick1] + " " + collumn2[pick2] + collumn3[pick3]
pc.copy(insult)
print(insult, "is kopierend naar het klembord.")
