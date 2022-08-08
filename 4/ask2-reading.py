# After reading this script, run it and see if you can succesfully cross the Bridge of Death

print("Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")

print()

name = input("What... is your name? ")
if name != "Sir Lancelot":
    print("(You are thrown off the bridge!) Auuuuuuuugh!!!")
else:
    # if name did equal "Lancelot"
    quest = input("What... is your quest? ")
    if quest != "To seek the Holy Grail":
        print("(You are thrown off the bridge!) Auuuuuuuuuuuuuuugh!!!")
    else:
        color = input("What... is your favourite colour? ")
        if color == "Blue":
            print("Go on. Off you go.")
        else:
            print("(You are thrown off the bridge!) Aaaaaauuuuuuuuuuuuuuugh!!!!!!!!!")


print()
