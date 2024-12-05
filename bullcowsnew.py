from random import choice
def number_generation():
    num=''
    m=[1,2,3,4,5,6,7,8,9]
    num+=str(choice(m))
    m.remove(int(num[-1]))
    m.append(0)
    for i in range(3):
        num+=str(choice(m))
        m.remove(int(num[-1]))
    return num
    
def comparing(number):
    while True:
        number=str(number)
        try:
            n=input('введите четырёхзначное целое число -> ')
            if n.lower().strip() =='нет':
                return False
            n=str(int(n))
            if len(n)==4:
                countbull, countcows=0, 0
                for i in range(4):
                    if number[i]==n[i]:
                        countbull+=1
                    elif n[i] in number:
                        countcows+=1
                if countbull==4:
                    return 'WIN'
                print(f'в этом числе {countbull} быков(-a) и {countcows} коров(-ы)\n')
                return int(n) 
        except:
            pass
def defchoiceuser():
    choiceuser=None
    while choiceuser not in ('да', 'нет'):
        try:
            choiceuser=input('введите да или нет ').lower().strip()
        except:
            pass
    d={'да':1,'нет':0}
    return d[choiceuser]
print('Приветствуем в игре Быки и коровы!\nВаша задача отгадать четырёхзначное число, мы поможем Вам сообщая \
сколько в введённом Вами числе быков и коров.\nБык - цифра стоит на своём месте, корова - такая цифра есть в загаданном \
числе, но у Вас она стоит не на своём месте :(\n')
print('ВНИМАНИЕ! Вы можете закончить игру в момент считывания числа если введёте нет\n')
while True:
    num=number_generation()
    count=0
    print('Давайте начнём!\nМы загадали число\n')
    print(num)
    while True:
        count+=1
        print(f'Ваша {count} попытка')
        uin=comparing(num)
        if uin=='WIN':
            print(f'Поздравляем! Вы выиграли c {count} попыток(-ки). Отличный результат!\n')
            print('Сыграем ещё?')
            key=defchoiceuser()
            break
        else:
            key=uin
        if not(key):
            break
    if not(key):
        print('Приходите ещё поиграть!')
        break
