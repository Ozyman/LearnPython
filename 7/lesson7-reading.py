# Most programs are read many more times than they are written (as bugs are fixed, features are added, etc.), so making a program easy to read is critical.
# Good comments make code easier to read and maintain.  You might think that a professional programmer spends all their time writing new code, but 
# actually a lot of time is spent 'maintaining' existing code.
# Maintance usually describes work which is done to fix bugs, and make updates and improvements on code that already accomplishes its primary task.

# A good comment describes not what is done, but why it is being done.  
# Which of these next two comments & code blocks to you think is more useful to someone who is reading the code?

# Set password to 6022140857
password = 6022140857

# Set password to Avogadro’s number which is Alexei's favorite number
password = 6022140857


# Another critical factor in readability/maintainability (besides good comments) is the use of functions

# A function is a little bit of code that can be reused over and over.  
# It's given a name, and you just use the name of the function to run the code that is in the function.

# You can identify functions, because they have parenthesis when they are used.
# We've used a few functions already.  The first function we used was print().
# Other functions include input() and random.choice().
# Can you think of other functions you've used?


# In addition to using functions that are built into python, or that are included with a python library, you can write your own functions.

# To create a new function, use the define (def) command.  Here we create a function called printNES() which prints the first two verses of "Never Ending Story".
def printNES():
    print("Turn around")
    print("Look at what you see")
    print("In her face")
    print("The mirror of your dreams")
    print("")
    print("Make believe I'm everywhere")
    print("Given in the light")
    print("Written on the pages")
    print("Is the answer to a never ending story")
    print("Ahahah ahahah ahahah...")
    print("")
    print("")


# If the program had to print the lyrics often, it would be useful to put the print statements into a function.  
# Each time you want to print the lyrics, instead of **Eleven** lines of print(), you just write printNES() once.

# Read the rest of this program.  Predict what it will do, then run it to make sure you understand.  
# After you run it come back and read the additional comments below.

print("Let's sing a song:")
printNES()

print("I want to hear it again!")
printNES()

again = input("Want to hear it again? (yes/no) ")
while(again != "no"):
    printNES()
    again = input("Want to hear it again? (yes/no) ")


# Imagine if we didn't have the printNES() function! 
# This short program would be much longer and harder to read.

# Imagine if we had wanted to print the entire song instead of just 2 verses.  Because we have this function, we can make the change in one place.  
# Without the function we would have to make the change in 3 places. 




