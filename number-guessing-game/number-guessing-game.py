import numpy as np

random_number = np.random.randint(0,100)

print("Guess a random number between 1-100")

while True:
    user_input = int(input("> "))
    if user_input == random_number:
        print(f'Correct, the number was {random_number}')
        break
    elif user_input > random_number:
        print("Too high")
    elif user_input < random_number:
        print("Too low")
    else:
        print("error")
