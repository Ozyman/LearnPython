# Read this code, and try to understand what will happen when you run it, then run the code and see if you were correct.
# If you didn't predict it correctly, review the code to identify your misunderstanding.

correct_guess = 42

guess = input("Guess a number between 1 and 100: ")

# The input() function always returns a string.  Even if you enter a number, it's stored as a series of characters.
# Python can't compare a string to an integer (e.g. correct_guess), so you first need to convert the guess to an integer.
# The int() function converts a string to an integer
guess_int = int(guess)

while guess_int != correct_guess:
    if guess_int < correct_guess:
        print("You guessed too low.")
    if guess_int > correct_guess:
        print("You guessed too high.")
    print("Try again!")
    guess = input("Guess a number between 1 and 100: ")
    guess_int = int(guess)

# Similarly, if we want to combine two strings, they both have to be strings.  It won't work if one is an integer.
# So we convert correct_guess to a string before combining it with another string
correct_guess_str = str(correct_guess)
print("You guessed it!  My number was " + correct_guess_str)    

# We didn't have to use a variable 'correct_guess' to store the value 42.  Instead, everywhere we put 'correct_guess' we could put 42 instead, and it would work exactly the same.
# The advantage to using a variable is that if we want to change the correct guess, we only have to change it in one place, instead of 4 different places.
