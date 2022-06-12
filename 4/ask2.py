# We are going to ask the user a question and put their answer into a variable
favorite_color = input("What is your favorite color? ")


# Now we want to respond in different ways depending on how the user answered our question.

# If blue is their favorite color (i.e. if the value stored in the favorite_color variable is equal to the string "blue"),
# we tell them it's our favorite also, otherwise we tell them we prefer blue.

# We use the special words 'if' and 'else' to define what we are checking, and what to do if it is true or false.

# After the lines with 'if' and 'else', the next line is indented to show that it goes with the if/else line above.

if favorite_color == "blue":
    print("That's my favorite too!")
else:
    print("I prefer blue.")

# go ahead and run this program now to see how it works.  Try running it a couple times and try giving different
# answers.  Can you get the program to give both responses?

# If you didn't already try typing "Blue" (With a capitol 'B'), try that.  Why does the program respond the way it does?

# After you've run the program a few times, then you are going to modify it.
# You are going to add a condition so that it also works with a capital 'B' -> "Blue"

# To do this we want the conditional to check if the favorite_color is "blue" or "Blue".
# Change the 'if' statement on line 14 above to look like this and rerun the program:
# if favorite_color == "blue" or favorite_color == "Blue":

# notice that this next line would not work:
# if favorite_color == "blue" or "Blue":

# 'or' can only be used to join two conditionals that are complete and independent.  
# It can not be used to compare one variable against two different things.

# You can even add a third (or more conditions) like this:
# if favorite_color == "blue" or favorite_color == "Blue" or favorite_color == "BLUE":



# If the user's favorite color isn't blue, you can add additional if statement to check another color. 
# This example code below says if condition1 is true, then do_thing().  If it's not true than check if condition2 is true.
# If condition1 was false and condition2 was true, than do_other_thing().
# Finally if both condition1 was false, and condition2 was also false, do_third_thing()
'''
if (condition1):
  do_thing()
else: 
  if (condition2):
    do_other_thing()
  else:
    do_third_thing()
'''

# Let's take a break from if & else for a second...
# You may have noticed that this example code doesn't have a # sign at the beginning, 
# but it still doesn't do anything when the program is run.
# Having three quotes all together like shown above can be used to start/end a block that 
# acts like a multi-line comment.

# Usually you just use a '#' on each line, even if you have a multi line comment,
# but sometimes it can be easier to add a ''' before and after several lines to turn the entire block into a comment.

'''
You can use normal quotes (") like above or single quotes ('),
like this example.  They work the pretty much the same.
''' 



# Back to the if & else stuff...
# The pattern of using another if statement after an else is so common, that it has a shortcut.
# 'elif' acts like an 'else' combined with another 'if'
# This code below does the same thing as the code above
"""
  if (condition1):
    do_thing()
  elif: (condition2):
    do_other_thing()
  else:
    do_third_thing()
"""


# Now that you've learned about if & else - go back to the original code, and modify it
# to give a different response for another color using the if, elif, else structure


# If you got all that working, congratulations!  Go check out the ask2-challenge.py for some additional practice.

