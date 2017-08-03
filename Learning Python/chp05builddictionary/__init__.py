#sample dictionary program

#empty dictionary, name it 'age'
age={}

#Add names to dictionary
age['Anna']=20
age['Portia']=19
age['Ambrose']=65
age['Allain']=45

#Use function has_key(), it takes this form:
#function_name.has_key(key-name)
#It returns TRUE if the dictionary has a key-name in it
#and returns FALSE if it doesn't.

if age.has_key('Anna'):
    print "Anna is listed in the dictionary. She is",\
    age['Anna'],"years old" #don't need space after "She is" and before "years old", list automtically has one
else:
    print "Anna is not listed in the dictionary"
    
if age.has_key('Portia'):
    print "Portia is listed in the dictionary. She is",\
    age['Portia'],"years old"
else:
    print "Portia is not listed in the dictionary."
    
if age.has_key('Allain'):
    print "Allain is listed in the dictionary. He is",\
    age['Allain'],"years old"
else:
    print "Allain is not listed in the dictionary"
    
if age.has_key('Althea'):
    print "Althea is listed in the dictionary. She is",\
    age['Althea'],"years old"
else:
    print "Althea is not listed in the dictionary"
    
#Use the function keys()-
#This function returns a list of all keys.

print "The following are listed in the dictionary:"
print age.keys() #no comma above, so names appear on separate line in output

#Use this function to put all key names in a list:
keys = age.keys()

#You can get a list of all values in a dictionary.
#use the function values():
print "The following are their ages:",  #comma here, will print values in same line in output
print age.values()

#put values in a list too
values = age.values()

#Sort lists with sort() function
#sort values in a list
#If use sort() in keys, will only arrange everything
#in alphabetical order, values listed in ascending order
#names and ages won't match, need create code will assign
#value to its real key

print keys
keys.sort()
print keys

print values
values.sort()
print values

#Find number of entries in dictionary with len() function
print "The dictionary contains", len(age), "entries."
