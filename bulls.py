def defchoiceuser():
    choiceuser=None
    while choiceuser not in (0, 1):
        try:
            choiceuser=int(input('1-да 0-нет '))
        except:
            print('вводите 0 или 1')
    return choiceuser
a=defchoiceuser()
print(a)