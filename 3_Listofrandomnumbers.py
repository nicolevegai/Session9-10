import random
def new_list():
    a = [] //creo la lista
    for i in range (0,random.randint(2,190)):
        number = random.randint(0,1000)
        a.append(number)   // agregoa. lista
    return a
my_list = new_list()
my_list.sort()
print(my_list[-1]) #-1: you get the last element of the list
yo lo hice así:
#Write a function that creates a list of random number of random

import random
def randlistcreator ():
    a = []

    for i in range (0, random.randint(2,100)): # se crea en numero random de lementos de la lista
        number=random.randint(1,1000) # se crean los elementos random
        a.append (number) # agrego los elementos randome creados a la lista
    return a
print (randlistcreator())
