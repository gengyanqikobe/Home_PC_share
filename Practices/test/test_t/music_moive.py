import threading
from time import ctime,sleep

def Music(music):
    for i in range(0,2):
        print('我听了%s. %s'%(music,ctime()))
        sleep(1)

def Moive(moive):
    for i in range(0,2):
        print("我看了电影%s. %s"%(moive,ctime()))
        sleep(5)



if __name__ == '__main__':
    Music("sugar")
    Moive("lord")
    print("我都看完了. ",ctime())