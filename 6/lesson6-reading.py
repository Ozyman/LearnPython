# Read this code, and try to understand what will happen when you run it, then run the code and see if you were correct.
# If you didn't predict it correctly, review the code to identify your misunderstanding.

# The guessing game from last lesson is a bit boring, because it always has the same answer
# This time we made a small change to improve it.
# We can use a function called randint() to get a random integer.
# This function is in the random library.  To get access to the functions in this library, we first need to put an import statement in the code.
import random

# Now we have access to the random library and the randint() function which is in the library.  
# Instead of always setting correct_guess to 42, we want to set it to a random integer between 1 & 42.
# randint takes two parameters, a minimum value and a maximum value
correct_guess = random.randint(1,100)

# We are also going to add a bit of excitement when they get it right.
# We are creating a new function to print a message several times.
# This defines the function, but nothing happens until we actually call it at the end of the program
def printSeveralTimes(msg, num_times):
    times_printed=0
    while(times_printed < num_times):
        print(msg)
        times_printed = times_printed + 1


guess = input("Guess a number between 1 and 100: ")
guess_int = int(guess)

while guess_int != correct_guess:
    if guess_int < correct_guess:
        print("You guessed too low.")
    if guess_int > correct_guess:
        print("You guessed too high.")
    print("Try again!")
    guess = input("Guess a number between 1 and 100: ")
    guess_int = int(guess)

correct_guess_str = str(correct_guess)
print("You guessed it!  My number was " + correct_guess_str)    


printSeveralTimes("Yay!!!!!!", 10)

















