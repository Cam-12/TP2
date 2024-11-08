BASE= 4
fromage= 800.0
eau= 2
ail= 2
pain= 400

nbConvives= int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
print("Pour faire une fondue fribourgeoise pour", nbConvives, "personnes, il vous faut :")

qfromage= fromage * nbConvives / BASE
print("-", qfromage, "gr de fromage")

qeau= eau * nbConvives / BASE
print("-", qeau, "dl d'eau")

qail= ail * nbConvives / BASE
print("-", qail, "gousse(s) d'ail")

qpain= pain * nbConvives / BASE
print("-", qpain, "gr de pain")