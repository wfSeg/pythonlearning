#there's also the "Not" operator, opposite day

#order of operation: Not, And, Or
#sample program

response='Y'
ans="Yes"

if ans=="Yes":
    print "This is just a test!"
    
number_one = int(raw_input("Enter a number: "))
number_two = int(raw_input("Enter another number: "))

if number_one > number_two:
    print "The first number is bigger"
elif number_two > number_one:
    print "The second number is bigger"
else:
    print "The numbers are equal"