from random import randint
def number_generation(level):
    if level == 1:
        number = randint(1, 10)
        attempts = 4
        st, end = 1, 10
    if level == 2:
        number = randint(1,25)
        attempts = 5
        st, end = 1, 25
    if level == 3:
        number = randint(1,50)
        attempts = 6
        st, end = 1, 50
    return number, attempts, st, end
def defchoiceuser():
    choiceuser=None
    while choiceuser not in (0, 1):
        try:
            choiceuser=int(input('1-да 0-нет '))
        except:
            print('вводите 0 или 1')
    return choiceuser
