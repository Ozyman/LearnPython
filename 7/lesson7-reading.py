# Most programs are read many more times than they are written (as bugs are fixed, features are added, etc.), so making a program easy to read is critical.
# This is also why comments are so important.  A good comment describes not what is done, but why it is being done.  



# We are also going to add a bit of excitement when they get it right.
# We are creating a new function to print a message several times.
# This defines the function, but nothing happens until we actually call it at the end of the program
def printSeveralTimes(msg, num_times):
    times_printed=0
    while(times_printed < num_times):
        print(msg)
        times_printed = times_printed + 1

