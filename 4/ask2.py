# We are going to ask the user a question and put their answer into a variable
favorite_color = input("What is your favorite color? ")


# Now we want to respond in different ways depending on how the user answered our question.

# If they like blue, we tell them it's our favorite also
# otherwise we tell them we prefer blue 
# After the lines with 'if' and 'else', the next line is indented to show that it goes with the if/else line above.

if favorite_color == "blue":
    print("That's my favorite too!")
else:
    print("I prefer blue.")

# go ahead and run this program now to see how it works.  Try running it a couple times and try giving different
# answers.  Can you get the program to give both responses?

# Once you've run the program a few times, you are going to modify it.

# If their favorite color isn't blue, you can add another if statement.  
# You'll have to indent the new 'if' under the else statement.  It should look like this:

"""
  if (condition1):
    do_thing()
  else:
    if (condition2):
        do_other_thing()
    else:
        do_third_thing()
"""

# You may have noticed that this example code doesn't have a # sign at the beginning, 
# but it still  doesn't do anything when the program is run.
# Having three quotes all together like shown above can be used to start/end a kind block that 
# acts like a multi-line comment.


'''
You can use normal quotes (") like above or single quotes ('),
like this example.  They work the pretty much the same.
''' 

 
# Now modify the code to give a different response for another color using the if, else/if, else structure
# 
# Can you ask the user another question, and say something in response?
# maybe ask how old they are.  Or if they like some TV show or what their favorite movie is.

