


#不同入参

#四个线程，每个线程执行五次
import threading
from time import ctime
import time

list_a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

def pr(times,ttt):

    for num in ttt:
        print("num is %d"%num,ctime())
        time.sleep(1)

def main():

    for i in list_a:

        t_pr = threading.Thread(target=pr,args=(5,i))
        t_pr.start()



if __name__ == '__main__':
    main()