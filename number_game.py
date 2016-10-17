import random

def game():
    # generate a random number between 1 and 10, inclusive
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        # get a number guess from the player
        guess = input("Guess a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("{} isn't an integer!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}.".format(guess))
        guesses.append(guess)
    # elses for while run whenever while finishes on its own
    ## As long as break or exception don't happen, the else will happen
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    # by using lower function we catch N and n
    #### TODO be able to accept all permutations of y,yes,n,no by stripping first letter
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()

# def make_num():
#     # generate a random number between 1 and 10, inclusive
#     secret_num = random.randint(1, 10)
#
# def check_val(num, secret_num):
#     if type(num) != int:
#         print("You did not enter an integer, please only use integers")
#         play_game()
#
#     # compare guess to secret number
#     if num == secret_num:
#         print("You got it! My number was {}".format(secret_num))
#         play_again()
#     # print hit/miss
#     elif num > secret_num:
#         print("Too high. Try again...")
#         play_game()
#     elif num < secret_num:
#         print("Too low. Give it another shot!")
#         play_game()
#
# def play_again():
#     # ask if player wants to play again
#     play = input("Would you like to play again? [Y / N]")
#
#     # if Y y yes or Yes, start game over, else quit
#     if play in ['Y', 'y', 'Yes', 'yes']:
#         print("Good luck, here you go again...")
#         play_game()
#     else:
#         print("Thanks for playing, see you next time!")
#         exit()
#
# play_game()
