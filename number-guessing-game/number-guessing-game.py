import numpy as np
v = "1.2.2" # version (displays on title screen).

# Global Stats
wins = 0
too_high = 0
too_low = 0

# title screen variable
title_screen = f"""- - - - - - - - - - - - - - - - - - - - - - - - - - - 
[1] EASY | [2] NORMAL | [3] HARD | [4] IMPOSSIBLE 
[5] CUSTOM | [6] AI MODE | [7] STATS | [8] ENDS GAME

version {v}
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""

# function for game code
def number_guessing_game(difficulty):

    # random number (selected by user)
    random_number = difficulty
    f_wins = 0 # when user selects correct number
    f_too_high = 0 # when user is too high
    f_too_low = 0 # when user is too low

    # while loop runs until random_number is guessed by user.
    while True:
        # user input (only takes ints).
        user_input = int(input("> "))

        # if user guesses correctly
        if user_input == random_number:  #
            print(f'You win! The correct number was {random_number}!')
            f_wins += 1 # adds +1 to f_wins when user guesses correct number.
            return f_wins, f_too_high, f_too_low # packs f stats (gets added to global stats outside of function).

        # if user guess is too high.
        elif user_input > random_number:
            print("Too high!")
            f_too_high += 1 # adds 1 to too_high counter

        # if user guess is too low.
        elif user_input < random_number:
            print("Too low!")
            f_too_low += 1 # adds 1 to too_low counter

        # for anything else.
        else:
            print("Error")

# function for AI model to guess instead of user
def ai_player_mode():
    print("Nothing here yet")


# prints title screen
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("Welcome to 'NUMBER GUESSING GAME'!") # this gets printed above title screen upon opening the game for the first time to welcome user.
print(title_screen) # this prints the rest of the title screen (with all the options and such).



# user selection mode
while True: # while loop so game doesn't end after game is finished.
    try:
        # this is the user selection to choose what option from the main title screen.
        user_mode_selection = int(input("> "))

        # selects "easy" mode.
        if user_mode_selection == 1: # selects the easy mode by the user.
            random_number = np.random.randint(0,10) # sets the random number
            print("Guess the random number between 0-10") # tells user (this is hard coded for each mode).
            f_wins, f_too_high, f_too_low = number_guessing_game(random_number) # inputs the random number into the function (that is then used for the game).
                                                                                # f_wins, f_too_high, etc stand for function wins, fucntion too_highs, etc. It takes the values from that game and sets these f to values.
            wins += f_wins # we then take the f values and ADD them to the global stats.
            too_high += f_too_high # this is done for all three.
            too_low += f_too_low # and again..
            print(title_screen) # title screen is shown again so user can select new game or exit.

        # selects "normal" mode.
        elif user_mode_selection == 2:
            random_number = np.random.randint(0,50)
            print("Guess the random number between 0-50")
            f_wins, f_too_high, f_too_low = number_guessing_game(random_number)
            wins += f_wins
            too_high += f_too_high
            too_low += f_too_low
            print(title_screen)

        # selects "hard" mode.
        elif user_mode_selection == 3:
            random_number = np.random.randint(0,100)
            print("Guess the random number between 0-100")
            wins, too_high, too_low = number_guessing_game(random_number)
            wins += f_wins
            too_high += f_too_high
            too_low += f_too_low
            print(title_screen)

        # selects "impossible" mode.
        elif user_mode_selection == 4:
            random_number = np.random.randint(0,1000000)
            print("Guess the random number between 0-1000000")
            wins, too_high, too_low = number_guessing_game(random_number)
            wins += f_wins
            too_high += f_too_high
            too_low += f_too_low
            print(title_screen)

        # select "custom" mode.
        elif user_mode_selection == 5:
            user_number_selection = int(input("Select custom number: "))
            random_number = np.random.randint(0,user_number_selection)
            print(f"Guess the random number between 0-{user_number_selection}")
            wins, too_high, too_low = number_guessing_game(random_number)
            wins += f_wins
            too_high += f_too_high
            too_low += f_too_low
            print(title_screen)

        # selects AI MODE
        elif user_mode_selection == 6:
            ai_player_mode()

        # prints the users stats. Vars listed above.
        elif user_mode_selection == 7:
            print(f"""
Stats:

wins --> {wins}
high guesses --> {too_high}
low guesses --> {too_low}
""") # these are the global stats (not f stats)

        # ends program.
        elif user_mode_selection == 7:
            print("Stopping program..")
            break # ends program

        # for anything else.
        else:
            print("error")

    except ValueError:
        print("Value Error.")


# add AI mode (one where it plays itself, one where it tries to guess the number first try).
# add HINTS where it gives a hint about the number. Ex) is the number divisible by 2? (yes/no).
# rounds counter (per game).
# perfect games (added to stats).
# some type of score
# achievements.
# AI stats.
# Add way for user to export and import their stats.
