import random
total=0
for i in range (0,10):
    number= random.randint(0,100)
    total= total+number
print("The sum of 10 random numbers is",+ total)
