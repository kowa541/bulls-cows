from random import randint
def number_generation(level):
    number = None
    if level == 1:
        number = randint(1, 10)
    if level == 2:
        number = randint(1,25)
    if level == 3:
        number = randint(1,50)
    return number