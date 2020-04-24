# Author: Sarah Oertly
# Date: 10/16/2019
# Description: Write a program that prompts the user for an integer that the player (maybe the user, maybe someone else)
# will try to guess. If the player's guess is higher than the target number, the program should display "too high" If
# the user's guess is lower than the target number, the program should display "too low" The program should use a loop
# that repeats until the user correctly guesses the number. Then the program should print how many guesses it took. When
# you run your program it should match the following format:
answer = int(input("Enter the number for the player to guess."))
guess = int(input("Enter your guess."))
guessed_it = False
i = 0

while not guessed_it:
    guess = int(input("Enter your guess."))
    i += 1
    if guess == answer:
        guessed_it = True
    if guess > answer:
        print("Too high - try again:")
    if guess < answer:
        print("Too low - try again:")
    if guess == answer:
        print("You guessed it in ", i, "tries")