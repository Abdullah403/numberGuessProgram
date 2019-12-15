# this is a pretty enjoyable "guess the numbers" game

import random

guessesTaken = 0

print("Hello!  What is your name?")
myName = input()

number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20")

for guesses_taken in range(6):
    print("Take a guess.")
    guess = input() 
    guess = int(guess) #the guess = input() returns a string so I need to convert the guess into an integer even though my input() will be a number
    guessesTaken += 1
    if guess < number:
        print("your guess is too low.")
    if guess > number:
        print("your guess is too high.")
    if guess == number:
        break

if guess == number:
    print("Good job, " + myName + "!  You guessed my number in " + str(guessesTaken) + " guesses!")

if guess != number:
    print("Nope, the number I was thinking of was " + str(number) + ", idiot.")
