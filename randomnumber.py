from random import randint
from math import log2
def level(lvl):
    rand=number_generation(lvl)
    text=['Вы в страхе убегаете от стада, но вдалеке видите груду камней!\
    \nОтгадайте число за 4 попытки, чтобы оббежать камни.','Не успев выдохнуть, вы уже видите приближающуюся стаю ворон!\
    \nОтгадайте число за 5 попыток, чтобы уклониться от птиц.', 
    'Вы устали и уже готовы быть затоптанным под десятком копыт,но вдалеке вы видите укрытие!\
    \nОтгадайте число за 6 попыток, чтобы укрыться от стада.']
    print(f'приветствуем на {lvl} уровне! \n{text[lvl-1]} заданный диапазон чисел {rand[2]}-{rand[3]}\n')
    for i in range(rand[1]):
        print(f'{i+1} попытка из {rand[1]}')
        result=comparing(rand[0])
        if result:
            return True
    print('попытки закончились и вас затоптали насмерть:(\
    \nвсю свою загробную жизнь вы прожили с паническим страхом быков и коров')
    return False
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
def comparing(number):
    while True: 
        flag=True
        user_input = input("Введите число ->  ")
        #На случай, если введено не целое число
        try:
            user_input = int(user_input)
        except ValueError:
            flag=False
        if flag: break
        print("Ошибка: введено не целое число. Пожалуйста, введите целое число.") 
    if user_input < number:
        print("Ваше число меньше загаданного.")
        return False
    elif user_input > number:
        print("Ваше число больше загаданного.")
        return False
    else:
        print("Ваше число равно загаданному.")
        return True
def defchoiceuser():
    choiceuser=None
    while choiceuser not in (0, 1):
        try:
            choiceuser=int(input('1-да 0-нет '))
        except:
            pass
    return choiceuser
print('Приветствуем в игре Быки и коровы!\nВам не посчастливилось наткнуться на стадо разъяренных быков и коров :(\
\nБегите и обходите препятствия, отгадывая числа!\n')
while True:
    for i in range(1, 4):
        if level(i):
            print('уровень пройден!')
            if i==3:
                print('Вы укрылись и выжили! Больше не натыкайтесь на стадо разъяренных быков и коров!!!')
                print('желаете сыграть снова?')
            else:
                print(f'желаете сыграть на {i+1} уровне?')
            choice=defchoiceuser()
            if not(choice):
                break

        else:
            print('желаете сыграть снова?')
            choice=defchoiceuser()
            break
    if not(choice):
        break
