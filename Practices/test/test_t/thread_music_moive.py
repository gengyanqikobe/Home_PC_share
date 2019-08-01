import threading
from time import ctime,sleep

def Music(music):
    for i in range(0,2):
        print('我听了%s. %s'%(music,ctime()))
        sleep(10)

def Moive(moive):
    for i in range(0,2):
        print("我看了电影%s. %s"%(moive,ctime()))
        sleep(1)

threadlist = list();

threadlist.append(threading.Thread(target=Music,args=("花好月圆",)))
threadlist.append(threading.Thread(target=Moive,args=("星际穿越",)))

if __name__ == '__main__':
    for thread in threadlist:
        thread.setDaemon(True)
        thread.start()

    for thread in threadlist:
#解决了第一个线程时间长没有结束，第二个线程结束直接导致父线程直接结束的问题
#join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞. join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程.
        thread.join()
    print('我全看完了',ctime())


