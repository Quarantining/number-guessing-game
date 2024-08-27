# Number Guessing Game
This is a simple number guessing game; the user is tasked to guess a random number based on the difficulty. Each time the user guesses, the program will tell the user if their guess was too high or too low. If the user guesses correctly, you are told so and the round ends. There are currently 6 modes;
- EASY - guess a number between 1-10
- NORMAL - guess a number between 1-50
- HARD - guess a number between 1-100
- IMPOSSIBLE - guess a number between 1-1000000 (million)
- AI mode - have an AI model guess the number for you. It will randomly guess between 1-1000.
- CUSTOM - set your own parameters.

The game also tracks your stats, including for the AI model! This includes your wins, total guesses, high guesses, and low guesses. The AI models stats are also separately tracked. 

There is also an option to exit a round, or the whole program. From the main menu, type "0" then confirm you want to exit. While in a round, the same process applies. Type 0 and confirm. (this is useful if you start an impossible round). 

# Future Plans
I plan to expand this program, adding a few more features. This includes a way to import and export your stats, so you don't lose all your progress each time you close the program. Also adding an intelligent AI model that attempts to guess the correct number using an algorithm instead of randomly guessing. Also adding a mode where the AI and the random number are random per guess, meaning the model must guess correctly first try. This would be known as a "perfect" game, and would also be an additional stat for both the player and AI model. Lastly, i'd like to try adding some type of hint system, where you can be told info about the number. For example, is the number divisible by 2? (yes/no). There may be more I also add (like achievements) but we'll see. (also maybe cheat codes, like being told what the random number is before even guessing).

# Program Purpose
Why am I coding this in the first place? For now, it's mostly for fun. This program has hardly challenged me the same way some of my other programs have, but I see it as a chance to review some of the concepts I already know. This program uses functions and if/elif trees to organize the code. I tried to make the code more organized by writing only 1 function for the actual game code that can be used with any number. So, if the argument is 10 the highest possible number will be 10 in the game. I also tried to clean up the code a bit with the if/elif tree, but I feel that there is probably more I can do to clean up the overall structure of the code. Comments are also quite messy, I added more than I personally need as I may show this to friends and family and I want them to also be able to understand what each thing in the program does. It might be a bit confusing because currently (as of update 1.2.4) there are a few variables that don't actually do anything, but are still tracked. Improving the readability will definitely be something I need to focus on in the future. There are also still a few errors, and I am sure there are more that I don't even know about yet. This gives me a chance to try "user testing," in other words.. making my friend try playing my game. Then getting user feedback and seeing how, or if I can improve.

This program was actually originally going to be part of a collection of simple programs, mostly coding problems rather than full scale projects. I was going to put all my projects into one folder to stay more organized (and I may still do this), but for now any full project has its own repo. This started to turn out to be more than just a simple coding exercise, and is now going to be treated as so. Because this was the only project in the repo, I just renamed the repo instead of moving it out into another (which I don't even know how to do yet). 

I hope that this program will challenge me to apply more logic when I add an AI model that tries to play smart, each turn guessing half as to minimize random guessing. We'll see how I attempt this!

Anyways~ that's it for now!
