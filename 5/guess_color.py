# Now we are going to try a guessing game

# First, We ask the user to guess a color.
color_guess = input("Can you guess the color I am thinking of? ")

# then if they didn't guess right, we keep giving them more tries until they get it right.
# because we want to do the same thing over and over again we are using a loop
# the "while" loop keeps doing something *while* the "condition" is true
# A "condition" is a statement that is true or false.  
# For example, in the 'ask2.py', we used this condition:
# favorite_color == "blue"

# That condition checks if two things are equal, but a condition can also check if two things are unequal.
# Just like == means "are these things equal?".  != means "not equal"
# 
# These next lines will check to see if color_guess is blue.  The loop will continue looping forever, while color_guess is not equal to "blue".
# just like the 'if' statement, the lines that go with the 'while' statement are indented to show they belong to it.  (The indended lines are called the "body" of the loop)
# In the "body" of the loop, the program asks the user to guess again, and gives them another chance.
# After asking them for a new guess, the while condition is checked again.  If color_guess is still not equal to "blue", then the user gets asked again, and the answer gets checked again, and so on forever...
# Or at least *while* the condition is true. 
# In this case the condition is true when color_guess is *not* equal to "blue".

while color_guess != "blue":
    color_guess = input("That's not it.  Guess again! ")

# If color_guess was equal to "blue", the condition would be false, and the while loop would "exit".  It would no longer go into the "body", and instead continues after the loop, and tells them they guessed right
print("You guessed right!")

# Try running the program.  Enter a few wrong answers, then enter "blue".

# What if the user enters "Blue" (i.e. with a capital 'B') does that work?
# go try it...
#
# ...
# ...
# ...
#
#
#
#
#
# computers are stupid - you have to tell them *exactly* what to do

# Change the message that is printed when they guess the correct color.  Tell them. "How did you know I was thinking of blue?"
# Run the program and make sure your change worked.

# Change the color that we want the user to guess.  Make sure to also change the color mentioned when they guess correctly.



