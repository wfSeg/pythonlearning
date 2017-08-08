from time import sleep
target=0
while target < 10:
    target=target+1
    sleep(1)
    print target
    
#unlike bash, sleep() needs to be imported