#example raw input

name=raw_input("Please type your name: ")
print "Hello %s" %name

person=raw_input("Name of the person to visit: ")
reason=raw_input("What is your purpose for visiting? ")

print "Good Day %s, you would like to see %s," % (name,person)
print "with the purpose of %s." % (reason.lower())