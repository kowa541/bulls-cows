from random import randint
def number_generation(level):
    if level == 1:
        number = randint(1, 10)
        attempts = 4
    if level == 2:
        number = randint(1,25)
        attempts = 5
    if level == 3:
        number = randint(1,50)
        attempts = 6
    return number, attempts