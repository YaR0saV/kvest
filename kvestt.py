from random import randint
import sys
import time



lnor = 10
hp = 100
rep = 20
mas = 30


def check_status(lnor, hp, rep, mas):
    if (rep > 100):
        print('\n Вы прошли игру!')
        sys.exit()
    if (hp <= 0):
        print('Вы проиграли.')
        sys.exit()
    if (rep <= 0):
        print('Вы проиграли.')
        sys.exit()
    if (mas <= 0):
        print('Вы проиграли.')
        sys.exit()
    if (lnor <= 0):
        print('Вы проиграли.')
        sys.exit()

def status(lnor, hp, rep, mas):        
    print('\n Репутация', rep)
    print(' Длина норы', lnor)
    print(' Ваше здоровье', hp)
    print(' Весс', mas)


def night(lnor, hp, rep, mas):
    print('\nНачинается ночь. Вы засыпаете.')
    lnor = lnor // 2
    hp = hp + 10
    rep = rep - 2
    mas = mas - 5
    print('')
    time.sleep(0.7)
    print('(∪｡∪)｡｡｡zzZ')
    time.sleep(0.7)
    print('(∪｡∪)｡｡｡zzZ')
    time.sleep(0.7)
    print('(∪｡∪)｡｡｡zzZ')
    time.sleep(0.7)

def nday():
    print('')
    print('Вы проснулись.')


def kopnor(lnor, hp):
    print('Как будете копть нору нору? \n 1. Интенсивно. \n 2. Лениво.')
    x = int(input())
    if x == 2:
        lnor = lnor + 2
        hp = hp - 15
    elif x == 1:
        lnor = lnor + 5
        hp = hp - 30
    else:
        print('Ошибка ввода \n Повторите заново.')
        return kopnor(lnor, hp)
    check_status(lnor, hp, rep, mas)
    night(lnor, hp, rep, mas)
    check_status(lnor, hp, rep, mas)
    nday()
    status(lnor, hp, rep, mas)
    activ(lnor, hp, rep, mas)


def eat(hp, rep, mas):
    print('Какую трава вас устроит? \n 1. Жухлая. \n 2. Зеленя.')
    z = int(input())
    if z == 1:
        hp = hp + 10
        mas = mas + 15
    elif z == 2:
        if rep < 30:
            print('Вас выгнали,лохи здесь лишние.')
            hp = hp -5
            rep = rep - 5
            mas = mas - 5
        else:
            hp = hp + 30
            mas = mas + 30
    else:
        print('Ошибка ввода \n Повторите заново.')
        return eat(hp, rep, mas)
    check_status(lnor, hp, rep, mas)
    night(lnor, hp, rep, mas)
    check_status(lnor, hp, rep, mas)
    nday()
    status(lnor, hp, rep, mas)
    activ(lnor, hp, rep, mas)



def fight(hp, rep, mas):
    print(' С кем бы вы хотели дрдьтся? \n 1. Со слабым. \n 2. С средним. \n 3. С сильным.')
    w = 0
    c = int(input())
    if c == 1:
        w = 30
    elif c == 2:
        w = 50
    elif c == 3:
        w = 70
    else:
        print('Ошибка ввода \n Повторите заново.')
        return fight(hp, rep, mas)
    rdhp = randint(0, mas + w)
    if rdhp >= mas: ## 1
        print('\nВы проиграли бой.')
        if (mas + rdhp) > w:
            rep = rep - 40
            hp = hp - 5
        elif mas == w:
            rep = rep - 10
            hp = hp - 10
        elif mas < w:
            hp = hp - 25
    if rdhp < mas:
        print('\nВы победили бой.')
        if mas > w:
            rep = rep + 2
        elif mas == w:
            rep = rep +5
            hp = hp - 1
        elif mas < w:
            rep = rep + 15
            hp = hp - 10
    check_status(lnor, hp, rep, mas)
    night(lnor, hp, rep, mas)
    check_status(lnor, hp, rep, mas)
    nday()
    status(lnor, hp, rep, mas)
    activ(lnor, hp, rep, mas)


def next_day():
    print('Вы решили прилечь днем.')
    check_status(lnor, hp, rep, mas)
    night(lnor, hp, rep, mas)
    check_status(lnor, hp, rep, mas)
    nday()
    status(lnor, hp, rep, mas)
    activ(lnor, hp, rep, mas)

def activ(lnor, hp, rep, mas):
    print('\n Что бы вы хотели сделать? \n 1.Копать нору \n 2.Поесть \n 3.Подраться  \n 4.Проспать день и ночь \n')
    y = int(input())
    if y == 1:
        print('\nВы пошли расширчять свой дом.')
        kopnor(lnor, hp)
    elif y == 2:
        print('\nВы проголодались. \nВы вышли на лужайку. ')
        eat(hp, rep, mas)
    elif y == 3:
        print('')
        fight(hp, rep, mas)
    elif y == 4:
        print('\nВас клонит в сон.')
        next_day()
    else:
        print('\nОшибка ввода \nПовторите заново.')
        return activ(lnor, hp, rep, mas)



print('Добро пожаловать в игру. \nЦель данной игры заключается в том, чтобы кролик остался живым и все на полянке его уважали.')
print('Load new game')
status(lnor, hp, rep, mas)
activ(lnor, hp, rep, mas)
