# Read this code, and try to understand what will happen when you run it, then run the code and see if you were correct.
# If you didn't predict it correctly, review the code to identify your misunderstanding.

noun1 = input("Please enter a noun: ")
noun2 = input("Please enter a plural noun: ")
verb = input("Please enter an action verb: ")
name = input("Please enter a name: ")


line1 = "Your mother was a " + noun1
line2 = "And your father smelt of " + noun2


print()  # <-- what does this line do?
print(name + ", I " + verb + " in your general direction.")
print(line1)
print(line2)
