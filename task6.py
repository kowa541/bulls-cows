from random import randint
def number_generation():
    return randint(1000, 9999)
def comparing(number):
    while True:
        number=str(number)
        try:
            n=input('введите четырёхзначное целое число -> ')
            if n.lower().strip() =='нет':
                return False
            n=str(abs(int(n)))
            if len(n)==4:
                countbull, countcows=[], 0
                for i in range(4):
                    if number[i]==n[i]:
                        countbull.append(i)
                for i in range(4):
                    for j in range(4):
                        if n[i]==number[j] and i not in countbull and j not in countbull:
                            countcows+=1
                            break
                if len(countbull)==4:
                    return 'WIN'
                print(f'в этом числе {len(countbull)} быков(-a) и {countcows} коров(-ы)\n')
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
print('Внимание! Вы можете закончить игру в момент считывания числа если введёте нет\n')
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

    
