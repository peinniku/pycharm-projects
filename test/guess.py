import random


def roll(num=3, points=None):
    print('<<<<<< ROLE THE DICE >>>>>>')
    if points is None:
        points = []
    while num > 0:
        point = random.randrange(1, 7)
        points.append(point)
        num -= 1
    return points


def result(total):
    if 3 <= total <= 10:
        return 'Small'
    else:
        return 'Big'


def start():
    money = 1000
    while money > 0:
        print('<<<<<< GAME STARTS >>>>>>')
        choices = ['Big', 'Small']
        choice = input('Big or Small:')
        bet = input('How much money do you want to bet:?')
        if choice in choices:
            points = roll()
            total = sum(points)
            win = choice == result(total)
            if win:
                print('The points are', points, 'You win')
                money += int(bet)
                print('You gain ', bet, ', you have ', money)
            else:
                print('The points are', points, 'You lose')
                money -= int(bet)
                print('You lose ', bet, ', you have ', money)
        else:
            print('invalid word')
            start()
    print('no money')


start()
