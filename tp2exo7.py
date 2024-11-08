import random

piece= random.randint(0, 100)
if piece < 66:
    print("Pile !")
else:
    print("Face !")