# Write a program that meets this requirements:
#
# Part 1:
# 1)  Ask the user to enter a food

# 2)  Print "I love to eat <food>"
#        Use the user input in the place of <food>
#
# Rewrite your program 

# Part 2:
# 1) Ask the user to enter a name, store a variable "name"
name = input("ENTER A NAME! ")
# 2) Ask the user to enter a number, store in a variable "number"
number = input("ENTER A NUMBER! ")
# 3) Ask the user to enter a noun, store in a variable "noun1"
noun = input("ENTER A NOUN! ")
# 4) Ask the user to enter a verb, store in a variable "verb"
verb = input ("ENTER A VERB! ")
# 5) Ask the user to enter another noun, store in a variable "noun2"
anothernoun = input ("ENTER ANOTHER NOUN! ")
# 6) Print a message that says:  Hi!  I am <name> and I am <number> years old. I have a <noun>.  I love to <verb> my <noun2>.  
#        Use the user input in the places indicated by <>.
othermessage = "Hi!  I am " + name + " and I am " + number +  " years old. I have a " + noun + "."  " I love to " + verb + " my " + anothernoun +  "."
print(othermessage)
# Try running this program (remember type: "python ask-challenge.py" in the shell)
