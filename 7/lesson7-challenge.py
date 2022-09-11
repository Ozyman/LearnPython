# In this lesson you will write three functions that will be used to generate a "madlibs" type story.
# and then prompt the user for words to use in the story.  

# NOTE: A sample story is provided in the commments, but feel free to change things however you'd like.

# write a function called print_introduction().
# It should take three variables: plural_noun, noun, and location.

# Then it uses those arguments to print the following sentence:
# Once upon a time there were three __plural_noun__.  They wanted to run away from home, so they packed up their __noun__,
# and ran away to go live in __location__


# write a function called print_middle().
# It takes plural_noun, verb, noun1, adjective, and noun2

# The __plural_noun__ loved to __verb__ in the __noun1__, and were so glad they had run away.  But one day a __adjective__ __noun2__
# showed up and they were scared!

# write a function called print_conclusion().
# It takes plural_noun, noun1, adjective1, noun2, noun3, and adjective2.

# The __plural_noun__ decided they should go back home.  When they got home their __noun1__ was so __adjective2__ to see them!
# They had a giant feast where they ate __noun2__ and __noun3__ and then went too bed early because they were so __adjective2__.


# there is one more function that will be defined in this script.
# It is given to you, because it does something you have not seen before.
# at the end of this function it has a 'return' statemnt.
# This allows the function to send back some data to the place where it was called.  
def get_word(word_type):

    word = input("Please enter a " + word_type + ": ")
    return word

# now that the functions are defined (above), we can call them.

# here is how we use get_word() to get the user input for the introduction
plural_noun = get_word("plural noun")
noun = get_word("noun")
location = get_word("location")

# Notice the difference between the variable: plural_noun and the string "plural noun".

# now that we have those three words, we can pass them to print_introduction()
# we have to make sure to pass the arguments in the same order they are listed in the function definition.
print_introduction(plural_noun, noun, location)

# now that you've seen how it is done, add the rest of the calls to get_word() to get the other words,
# and pass those words to print_middle() and print_conclusion()



