import os
from time import sleep
from termcolor import colored, cprint

point_a = 0
point_b = 0
turn = 1

def clean():
    sleep(2)
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

while(turn):
    clean()

    g = cprint('WELCOME TO ROCK, PAPER, SCISSORS!!', 'green', attrs = ['bold'])

    clean()

    cprint('PLAYER - 1 GET READY', 'grey', attrs = ['bold'])

    clean()

    bb = colored('PLAYER - 1', 'red', attrs = ['bold'])
    print(bb)
    h = colored('What is your choice? (1 : ROCK, 2 : PAPER, 3 : SCISSORS)', 'yellow')
    print(h)
    a = int(input('Choice: '))

    clean()

    cprint('PLAYER - 2 GET READY', 'grey', attrs = ['bold'])

    clean()

    bb = colored('PLAYER - 2', 'blue', attrs = ['bold', 'underline'])
    print(bb)
    h = colored('What is your choice? (1 : ROCK, 2 : PAPER, 3 : SCISSORS)', 'yellow')
    print(h)
    b = int(input('Choice: '))

    clean()

    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a== 3 and b== 2):
        cprint('PLAYER - 1 WINS THIS ROUND!', 'white', 'on_red')
        point_a += 1
    elif (a== b): 
        cprint('TIED ROUND!', 'white', 'on_yellow')
    else:
        cprint('PLAYER - 2 WINS THIS ROUND!', 'white', 'on_blue')
        point_b += 1
    
    clean()

    cprint('Play again? (1 : YES, 0 : NO)', 'magenta')
    turn = int(input('Choice: '))

clean()

cprint('CALCULATING RESULTS..', 'grey', attrs = ['bold'])

clean()

if(point_a > point_b):
    cprint('PLAYER - 1 WINS!', 'white', 'on_red')
elif(point_a == point_b):
    cprint('DRAW!', 'white', 'on_yellow')
else:
    cprint('PLAYER - 2 WINS!', 'white', 'on_blue')