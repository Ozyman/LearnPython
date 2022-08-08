# This program is going to generate a random person.

# We will need the random library for this so we import it
import random

# First, define the possible characteristics
hair_color = ["red", "brown", "blond"]
personality = ["mean", "friendly", "shy"]
skills = ["piano", "soccer", "drawing"]
name = ["Dustin", "Mike", "Nancy", "Joyce"]


# The random library has a choice() function that picks a random choice from a collection.

print(random.choice(name) + " is " + random.choice(personality) + ".  They have " + random.choice(hair_color) + " hair, and are good at " + random.choice(skills) + ".")


# Try running this a few times.
#
# 
#  Now we want to change some things.  Add a characteristic or two to each category, and add two more categories.
#  Then add another print statement to include your new categories.
# 

# Now for a more challenging change.  Instead of saying "They", change it to use their name again each time.    
# Try running it, did it work as expected?





