from sys import argv

# here the user has to put in the filename as the argument value
# when this python script is executed
script, filename = argv

# we open the file, given the filename and store it in the
# variable txt
txt = open(filename)

# We print out the content of the txt file with the .read command
print "Here's your file %r" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

txt.close
txt_again.close