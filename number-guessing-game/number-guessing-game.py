import numpy as np
v = "1.1"

# function for game code
def number_guessing_game(difficulty):

    # random number (selected by user)
    random_number = difficulty

    # while loop runs until random_number is guessed by user.
    while True:
        # user input (only takes ints).
        user_input = int(input("> "))

        # if user guesses correctly
        if user_input == random_number:  #
            print(f'Correct, the number was {random_number}')
            break  # ends program.

        # if user guess is too high.
        elif user_input > random_number:
            print("Too high!")
        # if user guess is too low.
        elif user_input < random_number:
            print("Too low!")
        # for anything else.
        else:
            print("Error")

# title screen
print(f"""Welcome to 'Number Guessing game'!

Please select difficulty:

easy --> 1
normal --> 2
hard --> 3
impossible --> 4  
custom --> 5   

version {v}
""")

# user selection mode
try:
    user_mode_selection = int(input("> "))

    # selects "easy" mode.
    if user_mode_selection == 1: # selects the easy mode by the user.
        random_number = np.random.randint(0,10) # sets the random number
        print("Guess the random number between 0-10") # tells user (this is hard coded for each mode).
        number_guessing_game(random_number) # inputs the random number into the function (that is then used for the game).
    # selects "normal" mode.
    elif user_mode_selection == 2:
        random_number = np.random.randint(0,50)
        print("Guess the random number between 0-50")
        number_guessing_game(random_number)
    # selects "hard" mode.
    elif user_mode_selection == 3:
        random_number = np.random.randint(0,100)
        print("Guess the random number between 0-100")
        number_guessing_game(random_number)
    # selects "impossible" mode.
    elif user_mode_selection == 4:
        random_number = np.random.randint(0,1000)
        print("Guess the random number between 0-1000")
        number_guessing_game(random_number)
    # select "custom" mode.
    elif user_mode_selection == 5:
        user_number_selection = int(input("Select custom number: "))
        random_number = np.random.randint(0,user_number_selection)
        print(f"Guess the random number between 0-{user_mode_selection}")
        number_guessing_game(random_number)
    # ends program.
    elif user_mode_selection == 6:
        print("Stopping program..")
    # for anything else.
    else:
        print("error")
except ValueError:
    print("Value Error.")
