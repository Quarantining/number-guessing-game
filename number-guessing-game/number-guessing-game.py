import numpy as np
v = "1.2"

# stats
wins = 0
too_high = 0
too_low = 0

# title screen
title_screen = f"""
Please select difficulty:

easy --> 1
normal --> 2
hard --> 3
impossible --> 4  
custom --> 5 

Stats --> 6
Stop game --> 7

version {v}
"""

# function for game code
def number_guessing_game(difficulty):

    # random number (selected by user)
    random_number = difficulty
    
    # when user selects correct number
    wins = 0
    
    # when user is too high
    too_high = 0
    
    # when user is too low
    too_low = 0

    # while loop runs until random_number is guessed by user.
    while True:
        # user input (only takes ints).
        user_input = int(input("> "))

        # if user guesses correctly
        if user_input == random_number:  #
            print(f'You win! The correct number was {random_number}!')
            wins += 1
            return wins, too_high, too_low # packs stats
            break  # ends program.

        # if user guess is too high.
        elif user_input > random_number:
            print("Too high!")
            too_high += 1 # adds 1 to too_high counter

        # if user guess is too low.
        elif user_input < random_number:
            print("Too low!")
            too_low += 1 # adds 1 to too_low counter
        # for anything else.
        else:
            print("Error")

# prints title screen
print("Welcome to 'Number Guessing game'!")
print(title_screen)

# user selection mode
while True:
    try:
        user_mode_selection = int(input("> "))

        # selects "easy" mode.
        if user_mode_selection == 1: # selects the easy mode by the user.
            random_number = np.random.randint(0,10) # sets the random number
            print("Guess the random number between 0-10") # tells user (this is hard coded for each mode).
            wins, too_high, too_low = number_guessing_game(random_number) # inputs the random number into the function (that is then used for the game).
            print(title_screen)

        # selects "normal" mode.
        elif user_mode_selection == 2:
            random_number = np.random.randint(0,50)
            print("Guess the random number between 0-50")
            wins, too_high, too_low = number_guessing_game(random_number)
            print(title_screen)
        # selects "hard" mode.
        elif user_mode_selection == 3:
            random_number = np.random.randint(0,100)
            print("Guess the random number between 0-100")
            wins, too_high, too_low = number_guessing_game(random_number)
            print(title_screen)
        # selects "impossible" mode.
        elif user_mode_selection == 4:
            random_number = np.random.randint(0,1000000)
            print("Guess the random number between 0-1000000")
            wins, too_high, too_low = number_guessing_game(random_number)
            print(title_screen)
        # select "custom" mode.
        elif user_mode_selection == 5:
            user_number_selection = int(input("Select custom number: "))
            random_number = np.random.randint(0,user_number_selection)
            print(f"Guess the random number between 0-{user_number_selection}")
            wins, too_high, too_low = number_guessing_game(random_number)
            print(title_screen)
        # prints the users stats. Vars listed above.
        elif user_mode_selection == 6:
            print(f"""
Stats:

wins --> {wins}
high guesses --> {too_high}
low guesses --> {too_low}
""")
        # ends program.
        elif user_mode_selection == 7:
            print("Stopping program..")
            break
        # for anything else.
        else:
            print("error")
    except ValueError:
        print("Value Error.")
