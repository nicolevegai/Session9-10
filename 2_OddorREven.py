def test (number, odd=True): #define function "test"
    if odd == True:
        if number % 2 == 1: #cuando el resto es 1 es odd
            return True
        else:
            return False
    else:
        if number % 2 == 0:
            return False
        else:
            return False

print(test(3))
