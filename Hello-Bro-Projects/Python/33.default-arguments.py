# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# # print(net_price(500))
# print(net_price(500, 0.1))

import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1) # how many seconds
    print("DONE!")
    
count(0, 10)

# the same result just exchange spots
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1) # how many seconds
    print("DONE!")
    
count(10)
