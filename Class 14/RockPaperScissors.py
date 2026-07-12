# rock paper scissors

import random

ch = ['rock','paper','scissors']
while True:
    cc = random.choice(ch)
    uc = input("enter your choice rock, paper, or scissors : ")
    if cc == uc:
        print("it is a tie")
    elif (uc == 'rock' and cc == 'scissors') or (uc == 'paper' and cc == 'rock') or (uc == 'scissors' and cc == 'paper'):
        print(" you win!!🏆")
    else:
        print("computer win❌")
    print(cc)
    ch2 = input("do you want to play again (y/n) : ")
    if ch2.lower() == 'n':
        break