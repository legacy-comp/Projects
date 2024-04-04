'''
Number Guesser:
simple mode: lower,higher
hard mode: too cold (>25),cold(12-25),hot(5-12),too hot(1-5)
'''
import random

def mod(num):
    if num < 0:
        return -num
    else:
        return num

random_num = random.randint(1,100)
game = True
total_guesses = 0
entered = []

while True:
    start = input("type 'start' to play the game\n")
    if start == 'start':
        break

if start == 'start':
    while True:
        mode = input("enter mode to play in (easy/hard):")
        if mode == 'easy' or mode == 'hard':
            break
    if mode == 'easy':
        while game:
            guess = input("enter your guess: ")
            if guess.isnumeric() == False:
                continue
            if int(guess) < random_num and guess not in entered:
                total_guesses += 1
                print("guess higher")
            elif int(guess) > random_num and guess not in entered:
                total_guesses += 1
                print("guess lower")
            elif int(guess) == random_num and guess not in entered:
                total_guesses += 1
                print(f"\nGotcha! you guessed {total_guesses} times\ncurrent number: {random_num}\ncurrent mode: {mode}")
                game = False
            if not guess in entered:
                entered.append(guess)
    elif mode == 'hard':
        while game:
            guess = input("enter your guess: ")
            if guess.isnumeric() == False or guess in entered:
                continue
            difference = mod(int(guess) - random_num)
            if difference >= 25:
                total_guesses += 1
                print("too cold")
            elif difference >= 12 and difference < 25:
                total_guesses += 1
                print("cold")
            elif difference >= 5 and difference < 12:
                total_guesses += 1
                print("hot")
            elif difference >= 1 and difference < 5:
                total_guesses += 1
                print("too hot")
            elif int(guess) == random_num:
                total_guesses += 1
                print(f"\nGotcha! you guessed {total_guesses} times\ncurrent number: {random_num}\ncurrent mode: {mode}")
                game = False
            if not guess in entered and guess.isalnum():
                entered.append(guess)