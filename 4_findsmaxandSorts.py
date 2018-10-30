import random
def randlistcreator ():
    a = []

    for i in range (0, random.randint(2,100)): # se crea en numero random
        number=random.randint(1,1000) # se crean los elementos random
        a.append (number) # agrego los elementos randome creados a la list
    return a

list=randlistcreator()
print (list)
      # hicetodo con la lalista random crada list para entender como funci
      # imprimio: [397, 388, 861, 154, 461, 595, 119]

def findmax(b=[]):
    a = b[0]
    pos = 0

    for i in range (len(b)):
        if b[i] > a:
            a =  b[i]
            pos = i

    return ( pos )

print (findmax(list)) #imprimio 2 porque es la posicion donde se encuenta 861

def my_sort (b=[]):
    result=[]
    while len(b)>0:
        pos=findmax(b)
        result.insert(0,b.pop(pos))

    return result

print (my_sort(list))  # imprimio [119, 154, 388, 397, 461, 595, 861]
