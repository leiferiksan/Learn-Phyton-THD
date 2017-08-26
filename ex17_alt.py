from sys import argv
from os.path import exists # with this command we can check whetere a
# file exists

scipt, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)

print "Alright, everything is done."
