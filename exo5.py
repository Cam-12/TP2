nombre=int(input("Entrez un nombre entier: "))
if nombre == 0:
    print("Le nombre est zéro (et il est pair)")
elif nombre > 0 and nombre % 2 == 0:
    print("Le nombre est positif est pair")
elif nombre > 0 and nombre % 2 == 1:
    print("Le nombre est positif est impair")

if nombre < 0 and nombre % 2 == 0:
    print("Le nombre est négatif est pair")
elif nombre < 0 and nombre % 2 == 1:
    print("Le nombre est négatif est impair")