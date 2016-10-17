# make a list of words
# pick a random word
# draw spaces
# take guess
# draw guessed letters and strikes
# print out win/lose

import random

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

while True:
    start = input("Press enter/return to start, or enter Q to quit")
    if start.lower() == 'q':
        break

    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(set(secret_word)):
        # draw spaces
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        # print blank line since above loop is on single line
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')

        # take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            # win if len(good_guesses) == UNIQUE characters in secret_word
            if len(good_guesses) == len(set(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)

    else:
        print("You didn't guess it! My secret word was {}".format(secret_word))
