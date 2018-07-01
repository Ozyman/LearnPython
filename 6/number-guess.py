# In the last program, you had to say exactly what color you wanted the user
# to guess.  And it was always the same every time the program was run.

# This time we are going to make a guessing game that changes everytime you run it.

# We don't have to write every bit of code ourselves to write a python program.
# Other people have written code that we can use.

# code is often organized into functions.  A function is a little bit of code
# that can be reused over and over.  It's given a name, and you just use the
# name of the function to make the program rerun the code that is in the function.

# You can identify functions, because they have parenthesis when they are used.
# We've used two functions so far.
# The first was print()
# The second function we used was input()
# Functions

#  Write a function to print something and call it several times.


# They put their code into "modules" which contain a bunch of code that does similar things

# This next line says we want to use the "random" module.  It lets us do things randomly - this will let the program do something different every time it is run.
import random



number_to_guess = random.randint(1,10)


guess = input("Guess a number between 1 and 10: ")
