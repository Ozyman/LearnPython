# This lesson will introduce two new concepts: f-strings & getting input from a file.
#
# f-strings are a more convenient way to build strings from variables.
# This is a simple program to illustrate

# First get two numbers from the user.  Since input() returns a string, we wrap it in a call to int() to immediately conver to an integer
num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))

print() # blank line to make it neater

# Then print some math facts for these numbers:
print(str(num1) + " + " + str(num2) + " = " + str(num1+num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1-num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1*num2))
print(str(num1) + " ^ " + str(num2) + " = " + str(num1**num2))

# NOTE: two asterisk are used for exponent.

print()  # put a blank line to make things neater


# Now we are going to do the print statements again, but with f-strings.
# You just need to put an f in front of the first quote
# Then in the string you can put {} with a variable (or an expresion) inside. 
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} ^ {num2} = {num1**num2}")

# f-strings are both easier to read and quicker to type, so they will be used in all lessons going forward.

# try running this program a few times to see that both blocks of print statements are equivalent.


# Once you've run it a few times we are going to show how you can use a file for input instead of having the user enter input on the keyboard.
# Take a look at the files input1.txt and input2.txt in this directory.
# Each of these files has two numbers in it.
# 
# We can have this script use the numbers in those files as the input to this script, by using the input redirection operator ('<') on the command line.
#
# start the script like this:
# python lesson8-reading < input1.txt
# 
# Once you get that working, see if you can run figure out how to run it with input2.txt.
#
# Finally, create a new file (input3.txt) and use that as your input.





