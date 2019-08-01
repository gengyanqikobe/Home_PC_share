
#用于程序判断是否继续进行
def Hesitate():

    temp_num = input("请输入 1 以继续执行程序，输入其他将退出程序：")
    if temp_num != '1':
        print("您选择了跳出")
        exit()