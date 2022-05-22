# We are going to ask the user a question and put their answer into a variable
#favorite_color = input("What is your favorite color? ")


# Now we want to respond in different ways depending on how the user answered our question.

# If blue is their favorite color (i.e. if the value stored in the favorite_color variable is equal to the string "blue"),
# we tell them it's our favorite also, otherwise we tell them we prefer blue.

# We use the special words 'if' and 'else' to define what we are checking, and what to do if it is true or false.

# After the lines with 'if' and 'else', the next line is indented to show that it goes with the if/else line above.

#if favorite_color == "blue" or favorite_color == "Blue" or favorite_color == "Blue." or favorite_color == "blue.":
  #  print("That's my favorite too!")
#else:
  #  print("I prefer blue.")

# go ahead and run this program now to see how it works.  Try running it a couple times and try giving different
# answers.  Can you get the program to give both responses?

# After you've run the program a few times, then you are going to modify it.

# If the user's favorite color isn't blue, you can add another if statement to check another color. 
# To do this we will use a new key word: 'elsif'
# This acts like an else combined with another 'if'

# This example code below says if condition1 is true, then do_thing().  If it's not true than check if condition2 is true.
# If condition1 was false and condition2 was true, than do_other_thing().
# Finally if both condition1 was false, and condition2 was also false, do_third_thing()
"""
  if (condition1):
    do_thing()
  elif: (condition2):
    do_other_thing()
  else:
    do_third_thing()
"""

# You may have noticed that this example code doesn't have a # sign at the beginning, 
# but it still doesn't do anything when the program is run.
# Having three quotes all together like shown above can be used to start/end a kind block that 
# acts like a multi-line comment.


'''
You can use normal quotes (") like above or single quotes ('),
like this example.  They work the pretty much the same.
''' 

 
# Now modify the code to give a different response for another color using the if, elif, else structure
# 
# Can you ask the user another question, and say something in response?
# maybe ask how old they are.  Or if they like some TV show or what their favorite movie is.

atla = input("Who's your favorite ATLA character? ")

if atla == "Toph" or atla == "Toph" or atla == "TOPH!":
    print("mine too! I love her! 'I AM THE MELON KING!' HehEehE")
elif atla == "Zuko":
    print('Oh, hes my second favorite!')

else:
    print("Oh! That's a cool character too! But I like toph better. Then zuko.")

