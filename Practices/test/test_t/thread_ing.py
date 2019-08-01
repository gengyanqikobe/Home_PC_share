import threading
from time import ctime,sleep
def fun(num):
    for i in range(0,int(num)):
        #输出这个线程的名字
        print('i come from %s,num :%s,%s'%(threading.current_thread().getName(),i,ctime()))
        sleep(1)

#fun(100)

def main(thread_num):
    thread_list = list()
    #先创建线程对象
    for i in range(0,thread_num):
        thread_name = "thread_%s"%i
        thread_list.append(threading.Thread(target =fun,name= thread_name, args = ('10',)))


    #启动所有线程
    for thread in thread_list:
        thread.start()

    #主线程等待所有子线程退出
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main(3)