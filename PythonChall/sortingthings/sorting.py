'''
Created on Oct 24, 2017

@author: Isador
'''

#TheQuiz = "L$O$N$G"

#can't copy paste from the website because there's \n newlines, need a way to split it
"""
count = 1
while (count > 0):
    user_input = input("enter in stuff: ")
    newlist = user_input.split('\n')
    newstring = ' '.join(newlist)
    Answer = newstring.translate(None, '!@#$%^&*(){}[]_+-=')

    print Answer
    count -= 1
print "Done Calculating...(dunno if it actually ran, have to put this here"
"""

#above not working, need a way to parse the mhtml file, instead of doing input
#actually, just copy the block to txt file and .split or .read it
'''
f = open('simpleparse.txt', 'r')
x = f.readlines()
#newlist = x.split('\n')
#newerlist = ' '.join(newlist)
#x.translate(None, '!@#$%^&*(){}[]_+-=')
print x
'''

# ok this one finally works, no /n
with open('simpleparse.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
print data
with open('parsethis.txt', 'r') as ohboy:
    bigdata=ohboy.read().replace('\n', '')
print bigdata
str(bigdata)
answer=bigdata.translate(None, '!@#$%^&*(){}[]_+-=?><')
print answer

# I did it!!! the answer is "equality" ... what?