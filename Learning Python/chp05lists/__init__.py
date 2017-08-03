#Tuples are static lists, data in it can't be changed

#example
months = ('Jan','Feb','Mar','Apr','May','Jun',\
          'Jul','Aug','Sep','Oct','Nov','Dec')

#Lists can be modified, it's "mutable"
dogs = ['Lucky','Snoopy','Bingo','Jacky','Magic']

#notice, it uses [] square brackets

print dogs[3]
print months[3]

#print range too with [:]
print dogs[1:4]

#append to list with 'append()'
dogs.append('Appendog')
print dogs[4:5]     #this doesn't print dog[5]
print dogs[5]       #this does. why?

#dictionary, like a phonebook
phone={'Catherine Becket':7895675, 'Anthony Clarke':1234523,\
       'Linda Jones':8875689, 'Andy Bower':7564438,\
       'Davey Lewis':5656789}
print phone['Catherine Becket']
phone['David King']=1231234
print phone['David King']

#this should delete dictionary entry, but will give error,
#because it works.
#del phone['Anthony Clarke']
#print phone['Anthony Clarke']