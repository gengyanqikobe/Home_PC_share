
import random
import sys

def xinyongma():
    temp = '1'
    for i in range(0,17):

        a = random.randint(1,9)
        temp = str(a)+temp
    return temp

#print(xinyongma())