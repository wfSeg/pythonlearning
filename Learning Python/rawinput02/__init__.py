#combining string operators and index

name = raw_input("What is your name? ")
first_letter=name[0].upper()    #this works


#rest=name-name[0]       #this doesn't, how to add rest of name, minus the first letter?
#do some math

total=len(name)
rest=name[total-1]


print "Your name is %s" % (first_letter+rest)