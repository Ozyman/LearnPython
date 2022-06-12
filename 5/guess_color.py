# In the last section (part 4), we tried writing some guessin games, but we only asked the user one time, and if they got
# the answer wrong they didn't get another chance to guess again.

# This time we are going to improve the guessing game and ask the user to keep guessing until they get the answer right.

# First, We ask the user to guess a color.
color_guess = input("Can you guess the color I am thinking of? ")

# then if they didn't guess right, we keep giving them more tries until they get it right.
# In programming when you want to do something many times, you can put it in a "loop".
# There are a few different kinds of loops, but first we are goin to learn about a "while" loop.

# The "while" loop keeps doing something *while* the "condition" is true
# A "condition" is a statement that is either true or false.  
# You've seen conditions before, because they are also used in "if" statements.
# For example, in ask2.py, we used this condition:
# favorite_color == "blue"

# That condition checks if two things are equal, but a condition can also check if two things are unequal.
# Just like == means "are these things equal?".  != means "not equal"
#
# So here is a similar condition:
# favorite_color != "blue"
# 
# In this case, the condition is true if favorite color is *not* "blue".  Which means it is false if favorite color is blue.
# The "not"  (i.e. '!') means the condition does the opposite of "==".


# These next lines will check to see if color_guess is blue.  As long as color_guess is not equal to "blue", this loop will continue forever.
# just like the 'if' statement, the lines that go with the 'while' statement are indented to show they belong to it.  (The indended lines are called the "body" of the loop)
# In the "body" of the loop, the program asks the user to guess again, and gives them a chance to try a new answer.
# After asking them for a new guess, the while condition is checked again.  If color_guess is still not equal to "blue", then the user gets asked again, 
# and the answer gets checked again, and so on forever...
# Or at least *while* the condition is true. 
# In this case the condition is true when color_guess is *not* equal to "blue".
while color_guess != "blue":
    color_guess = input("That's not it.  Guess again! ")


# When the user enters "blue, the color_guess variable will now be equal to "blue", and so the condition would be false, and the while loop would "exit".  
# The program would no longer go into the "body", and instead the loop is done, and it continues to this next line that tells the user that they guessed right
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

