

import threading
import time
from time import ctime

def sing(num):
    for i in range(num):
        print('sing%d'%i,ctime())
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print('dance%d'%i,ctime())
        time.sleep(0.5)
def main():
    #######创建启动线程
    t_sing = threading.Thread(target=sing,args=(5,))
    t_dance = threading.Thread(target=sing,args=(5,))
    t_sing.start()
    t_dance.start()

if __name__ =='__main__':
    main()