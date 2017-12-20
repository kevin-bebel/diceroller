#!/usr/bin/python3

import random

def rolldice():
    return random.randrange(1,7)

def ask():
    return input("Guess the Roll : ")

def main():
    name = ''
    while len(name) == 0:
        name = input("Hi,Whats your name? ")

    print("Ok {} Lets Play. Try to guess what the dice roll will be".format(name))

    while True:
        guessed = ask()
        roll = rolldice()

        if guessed == roll :
            print("Yay! You guessed right")
        else:
            print("Flip! You got it wrong. The Roll was {}".format(roll))

        answer = ''
        while answer == '':
            answer = input("Do you want to try again[y/n]? ")
            if answer.lower() == 'y':break
            elif answer.lower() == 'n': break
            else: answer = ''

        if answer.lower() == 'n':
            break

    print("Thanks for playing {}!. Goodbye!".format(name))

if __name__ == "__main__":main()
