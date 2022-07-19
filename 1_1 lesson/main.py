def count_sheeps(sheep):
  # TODO May the force be with you
    g = 0
    for element in sheep:
        if element == True:
            print(element)
            g = g +1
    return g


array1 = [True,  True,  True,  False,
        True,  True,  True,  True ,
        True,  False, True,  False,
        True,  False, False, True ,
        True,  True,  True,  True ,
        False, False, True,  True, True ]

print(count_sheeps(array1))