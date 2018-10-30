
import random
def randlistcreator ():
    a = []

    for i in range (0, random.randint(2,100)): # se crea en numero random de lementos de la lista
        number=random.randint(1,1000) # se crean los elementos random
        a.append (number) # agrego los elementos randome creados a la lista
    return a
print (randlistcreator())
