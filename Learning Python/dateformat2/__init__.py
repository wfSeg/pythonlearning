#time in mm/dd/yyyy format

from datetime import datetime

now=datetime.now()

print '%s/%s/%s'%(now.month,now.day,now.year)

print now.hour
print now.minute
print now.second

print '%s:%s:%s'%(now.hour,now.minute,now.second)

print '%s/%s/%s %s:%s:%s'%(now.month,now.day,now.year,now.hour,now.minute,now.second)
