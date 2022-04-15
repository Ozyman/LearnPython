# Now we are going to try a guessing game

# We ask the user to guess a color
color_guess = input("Can you guess the color I am thinking of? ")

# then if they didn't guess right, we keep giving them more tries until they get it right.
# because we want to do the same thing over and over again we are using a 'loop'
# the 'while loop' keeps doing the same thing *while* the "condition" is true
# A "condition" is something that is true or false.

# != means "not equal", so these lines will keep asking the user to guess a color while their guess is not 'blue'
# just like the 'if' statement, the lines that go with the 'while' statement are indented to show they belong to it.
while color_guess != "blue":
    color_guess = input("That's not it.  Guess again! ")
    


print("You guessed right!")

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

# Try to change the color that we want the user to guess.
# Change the program to guess something else.  Maybe a number or name of your best friend.


