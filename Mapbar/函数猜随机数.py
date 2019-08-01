def guess(num,a):
    if a==num:
        print('great')
        return True
    else:
        return False

    
from random import randint
a=randint(1,10)
c=False
while c!=True:
    num=int(input('please type the number :\n'))
    c=guess(num,a)
print('the random number is:%d'%num)
