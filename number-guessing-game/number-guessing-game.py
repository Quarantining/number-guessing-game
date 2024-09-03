import numpy as np
import os

v = "1.2.8" # version (displays on title screen).

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Global Stats
wins = 0
too_high = 0
too_low = 0
user_guesses = 0
fewest_guesses = 0
most_guesses = 0
perfect_games = 0

# AI (random) Global Stats
ai_wins = 0
ai_too_high = 0
ai_too_low = 0
ai_guesses = 0
ai_fewest_guesses = 0
ai_most_guesses = 0
ai_perfect_games = 0

# AI (intelligent) Global Stats
intelligent_wins = 0
intelligent_too_high = 0
intelligent_too_low = 0
intelligent_guesses = 0
intelligent_fewest_guesses = 0
intelligent_most_guesses = 0
intelligent_perfect_games = 0

# AI (perfect) global Stats
perfect_wins = 0
perfect_too_high = 0
perfect_too_low = 0
perfect_guesses = 0
perfect_fewest_guesses = 0
perfect_most_guesses = 0
perfect_ai_guesses = 0
most_correct_guesses = 0

# AI (hacks) Global Stats
hacks_wins = 0
hacks_too_high = 0
hacks_too_low = 0
hacks_guesses = 0
hacks_fewest_guesses = 0
hacks_most_guesses = 0
hacks_perfect_games = 0

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# title screen variable
title_screen = f"""- - - - - - - - - - - - - - - - - - - - - - - - - - - 
           > > > - -[MAIN MENU] - - < < <

[1] USER MODE [6] AI MODE | [7] STATS | [0] QUIT/END GAME


version {v}
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""

# welcome screen
welcome_screen = f"""- - - - - - - - - - - - - - - - - - - - - - - - - - - 
Welcome to 'NUMBER GUESSING GAME'!
{title_screen}"""

user_mode_screen = """
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
           > > > - -[USER MODE] - - < < <
Select Mode:
[1] EASY | [2] NORMAL | [3] HARD 
[4] IMPOSSIBLE | [5] CUSTOM | [0] QUIT

- - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""

# AI mode selection screen
ai_mode_screen = """
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
            > > > - -[AI MODES] - - < < <

Select Model:
[1] RANDOM | [2] INTELLIGENT | [3] PERFECT ONLY 
[4] HACKS | [7] STATS | [?] INFO | [0] EXIT

- - - - - - - - - - - - - - - - - - - - - - - - - - - 

"""

# gives a description about what each AI model does.
ai_model_info = """
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
            > > > - -[AI MODEL INFO] - - < < <
    
[1] RANDOM --> guesses randomly with no logic.
[2] INTELLIGENT --> guesses 50% between the highest possible value and the previous guess
[3] PERFECT ONLY --> both the AI guess and random number are randomly selected each game;
the AI must guess in 1 attempt.    
[4] HACKS --> the AI will always guess the correct number.   
[EXIT] --> returns you to main menu.
    
- - - - - - - - - - - - - - - - - - - - - - - - - - -                 
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# function for game code
def number_guessing_game():
    global wins, too_high, too_low, user_guesses
    print(user_mode_screen)

    difficulty_selection = int(input("> ")) # input to select difficulty.
    max_num = 0 # sets the maximum number that can be generated.

    if difficulty_selection == 1: # easy
        max_num = 10

    elif difficulty_selection == 2: # normal
        max_num = 50

    elif difficulty_selection == 3: # hard
        max_num = 100

    elif difficulty_selection == 4: # very hard
        max_num = 1000

    elif difficulty_selection == 5:
        max_num = int(input("Select maximum number: "))
    else:
        print("Error")

    random_number = np.random.randint(1, max_num)  # sets the random number
    print(f"Guess the random number between 1-{max_num}") # tells user to guess num between 0-{max_num}

    # while loop runs until random_number is guessed by user.
    while True:
        # user input (only takes ints).
        user_input = int(input("> ")) # 0 to end program, > 0 to guess number.

        if user_input == 0: # stops program
            confirm_stop = input("do you want to quit game? (yes/no): ") # confirms that user wants to quit
            if confirm_stop == "yes": # ends game
                print("game quit.")
                break
            elif confirm_stop == "no": # returns user game
                print("game not quit.")
            else: # if user doesn't type "yes" or "no"
                print("Error. returning to game.") # returns user to game.

        # if user guesses correctly
        elif user_input == random_number:
            print(f'You win! The correct number was {random_number}!')
            wins += 1 # adds +1 to f_wins when user guesses correct number.\
            user_guesses += 1 # adds guess
            print("[0] RETURN MAIN MENU [1] PLAY AGAIN.")
            user_input_after_win = int(input("> "))
            if user_input_after_win == 0:
                clear_screen()
                print(title_screen)
                break
            elif user_input_after_win == 1:
               clear_screen()
               print(user_mode_screen)

            else:
                print("Error")

        # if user guess is too high.
        elif user_input > random_number:
            print("Too high!")
            user_guesses += 1
            too_high += 1 # adds 1 to too_high counter

        # if user guess is too low.
        elif user_input < random_number:
            print("Too low!")
            user_guesses += 1
            too_low += 1 # adds 1 to too_low counter

        # for anything else.
        else:
            print("Error")

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# function for AI model to guess instead of user.
def ai_player_mode(difficulty):
    random_number = np.random.randint(1,1000) # var that sets random num.
    guess_count = 0 # times the AI guessed.

    f_ai_wins = 0  # when AI selects correct number
    f_ai_too_high = 0  # when Ai is too high
    f_ai_too_low = 0  # when AI is too low
    f_ai_guesses = guess_count
    try:
        for i in range(99999): # the AI gets 99999 attempts to guess the correct num.

            ai_guess = np.random.randint(1,1000) # ai guess is randomly generated.
            guess_count += 1 # adds +1 guess each iteration of for loop.

            if ai_guess == random_number:
                print(f"> {ai_guess}")
                print(f"You win! The correct number was {random_number}!")
                print(f"It took the AI {guess_count} attempts.") # prints the total attempts it took the AI to guess the correct num.
                f_ai_wins += 1
                return f_ai_wins, f_ai_too_high, f_ai_too_low, f_ai_guesses
            elif ai_guess > random_number:
                print(f"> {ai_guess}")
                f_ai_too_high += 1
                print("Too high!")
            elif ai_guess < random_number:
                print(f"> {ai_guess}")
                f_ai_too_low += 1
                print("Too low!")
            else:
                print("Error") # just incase

    except TypeError:
        print("Error")

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

def ai_intelligent_mode():
    print("Coming soon.")



def ai_perfect_mode():
    f_perfect_ai_guesses = 0
    attempts = 0
    f_most_correct_guesses = 0

    for i in range(1000):
        random_number = np.random.randint(1,1000)
        ai_guess = np.random.randint(1,1000)

        attempts += 1
        print(f"> {(str(ai_guess))} attempt: {attempts}")

        if ai_guess == random_number:
            print(f"You win! The correct number was {random_number}!")
            print(f"It took the model {f_perfect_ai_guesses} attempts to guess first try!")
            f_perfect_ai_guesses += 1
            f_most_correct_guesses += 1

        elif ai_guess > random_number:
            print(f"Too high! The correct number was {random_number}")

        elif ai_guess < random_number:
            print(f"Too low! The correct number was {random_number}")

        else:
            print("Error")
            break

    print(f"The PERFECT model was able to guess the correct number {f_perfect_ai_guesses} times in {attempts} attempts.")
    return f_perfect_ai_guesses, f_most_correct_guesses


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


def ai_hacks_mode():
    print("Coming soon.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


def plot_game_data():
    print("Coming soon.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


def hints():
    print("Coming soon.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


def stats_sum():
    print("Coming soon.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


# function that clears the screen.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

def user_stats_screen():
    # these are the global stats (not f stats).
    return  f"""
- - - - - - - - - - - - - - - - - - - - - - - - - - - 
            > > > - -[STATS] - - < < <

Your Stats:
    wins --> {wins}
    perfect wins --> 
    total guesses --> {user_guesses}
    high guesses --> {too_high}
    low guesses --> {too_low}

- - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""


def ai_stats_screen():
    # shows that stats of all AI models.
    return f"""
- - - - - - - - - - - - - - - - - - - - - - - - - - -
            > > > - -[AI STATS] - - < < <
AI Stats (RANDOM):
    wins --> {ai_wins}
    perfect AI wins --> 
    total AI guesses --> {ai_guesses}
    high guesses --> {ai_too_high}
    low guesses --> {ai_too_low}
    wins with fewest guesses -->
    wins with most guesses --> 
    
AI Stats (INTELLIGENT):
    wins --> {intelligent_wins}
    perfect AI wins --> {intelligent_perfect_games}
    total AI guesses --> {ai_guesses}
    high guesses --> {intelligent_too_high}
    low guesses --> {intelligent_too_low}
    wins with fewest guesses --> {intelligent_fewest_guesses}
    wins with most guesses --> {intelligent_most_guesses}

AI STATS (PERFECT):
    wins --> {perfect_wins}
    perfect AI wins --> {perfect_ai_guesses}
    total AI guesses --> {perfect_guesses}
    high guesses --> {perfect_too_high}
    low guesses --> {perfect_too_low}
    wins with fewest guesses --> {perfect_fewest_guesses}
    wins with most guesses --> {perfect_most_guesses}

AI STATS (HACKS):
    wins --> {hacks_wins}
    perfect AI wins --> {hacks_perfect_games}
    total AI guesses --> {hacks_guesses}
    high guesses --> {hacks_too_high}
    low guesses --> {hacks_too_low}
    wins with fewest guesses --> {hacks_fewest_guesses}
    wins with most guesses --> {hacks_most_guesses}

- - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

# is set to True when selecting model, when set back to false
# returns user to main menu.
in_ai_menu = False

# prints title screen
print(welcome_screen) # this gets printed once upon opening game.

# user selection mode
while True: # while loop so game doesn't end after game is finished.
    try:
        # this is the user selection to choose what option from the main title screen.
        user_mode_selection = int(input("> "))
        clear_screen()

        # selects "easy" mode.
        if user_mode_selection == 1: # selects the easy mode by the user.
            number_guessing_game() # inputs the random number into the function (that is then used for the game).

        # selects AI MODE
        elif user_mode_selection == 6:

            in_ai_menu = True # while True user will be stuck in AI menus
            print(ai_mode_screen) # prints the AI menu screen

            while in_ai_menu == True:

                ai_mode_select = input("> ") # prompts user to select AI mode.

                if ai_mode_select == "1": # random
                    f_ai_wins, f_ai_too_high, f_ai_too_low, f_ai_guesses = ai_player_mode(1000)
                    ai_wins += f_ai_wins
                    ai_too_high += f_ai_too_high
                    ai_too_low += f_ai_too_low
                    ai_guesses += f_ai_too_low + f_ai_too_high
                    print(ai_mode_screen)

                elif ai_mode_select == "2": # intelligent
                    print("Coming soon..")

                elif ai_mode_select == "3": # perfect only
                    f_perfect_ai_guesses, f_most_correct_guesses = ai_perfect_mode() # takes f_perfect_ai_guesses (number of guesses the ai made) & f_most_correct_guesses (the amount of times it correctly guessed the number).
                    perfect_wins += f_perfect_ai_guesses # adds perfect wins to global perfect ai stats
                    perfect_ai_guesses += f_perfect_ai_guesses # also adds perfect games to normal wins (because it can only win a perfect game).

                    if f_most_correct_guesses >= perfect_most_guesses: # checks how many perfect games it won in a single session.
                        perfect_most_guesses = f_most_correct_guesses # if its greater or equal, the stats get updated (replaced). This is to show its best session, not total sessions (unlike most other stats).
                        print(f"New High Score! Your model guessed {perfect_most_guesses} in a single game!")
                    else: # otherwise, the decision tree ends.
                        print(f"No new scores. Your highest score is still {perfect_most_guesses}.")

                    print(ai_mode_screen)

                elif ai_mode_select == "4": # hacks
                    print("Coming soon..")

                elif ai_mode_select =="?": # info
                    print(ai_model_info)

                elif ai_mode_select == "7":
                    print(ai_stats_screen())

                elif ai_mode_select == "0":
                    in_ai_menu = False
                    print("returning to MAIN MENU")
                    print(title_screen)

                else:
                    print("Error")


        # prints the users stats. Vars listed above.
        elif user_mode_selection == 7:
            print(user_stats_screen()) # these are the global stats (not f stats)

        # ends program.
        elif user_mode_selection == 0:
            confirm_stop = input("Do you want to quit program? Your stats wont be saved. (yes/no): ") # checks with user to confirm quiting

            if confirm_stop == "yes": # if user types "yes"
                print("program stopped.") # tells user program is stopping
                break # ends program

            elif confirm_stop == "no": # if user types "no"
                print(title_screen) # program does not stop

            else: # for any other input
                print("Error") # prints an error message

        # for anything else.
        else:
            print("error")

    except ValueError:
        print("Value Error.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


# [Ideas List]:
# add intelligent ai model that guesses half way between the highest possible number and lowest guess.
# add a perfect model where the guess and random number are both random, meaning the AI needs to guess corectly on it's first try.
# add a hacks model that always guesses the number correctly.
# add a way to plot the stats of each AI model onto a graph.
# add a way to import and export user/ai stats with a txt file (or something similar).
# add intelligent hints that give the user clues about what type of number they are guessing (like is it odd, even, etc).
# add a game score and level system.
# add achievements.
# add cheats ex) tells you what the correct number is before guessing.
# add easter eggs
# add function to sum stats after each game.
# add a clear stats function (per model) that is password protected.
# clear the screen after each game as keep menus more readable.
