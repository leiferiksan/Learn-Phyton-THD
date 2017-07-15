from sys import argv
# add the feature/module/library sys
# and import the argument variable to the script 

script, first, second, third = argv # here we unpack the argument

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

confuse = int(raw_input("What was your first argument again?"))

print "That is %s." % (confuse == int(first) # why is this false when I type in first?