import os
os.system('cls')
from random import randint

t = ["Rock", "Paper", "Scissors"]

i = 0
Robot = 0
Person = 0
number = input("Enter number of game turns? ")
n = int(number)
flag = True

while (flag):
    computer = t[randint(0,2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("--> Tie! \U0001F917")
            print()
        elif player == "Rock":
            if computer == "Paper":
                print("--> You lose!", computer, "covers", player)
                print()
                Robot+=1
            else:
                print("--> You win!", player, "smashes", computer)
                print()
                Person+=1
        elif player == "Paper":
            if computer == "Scissors":
                print("--> You lose!", computer, "cut", player)
                print()
                Robot+=1
            else:
                print("--> You win!", player, "covers", computer)
                print()
                Person+=1
        elif player == "Scissors":
            if computer == "Rock":
                print("--> You lose...!", computer, "smashes", player)
                print()
                Robot+=1
            else:
                print("--> You win!", player, "cut", computer)
                print()
                Person+=1
        else:
            print("--- That's not a valid play. Check your spelling! PLEASE TRY AGAIN \U0001F92A ---")
            print()
        player == False
        computer = t[randint(0,2)]
        if Robot == n:
            flag = False
        elif Person == n:
            flag = False

if Robot > Person:
    print("==>> You Lose! \U0001F614")
else:
    print("==>> You Win! \U0001F60D")