



#本py文件用于将字符串转化为特德key：value格式

def trans():
    str_test = input("请输入要转化的字符串：")
    list_a = []
    list_b = []

    for i in str_test.split('&'):
        list_a.append(i)

    #print(list_a)

    for j in list_a:
        k = j.split('=')[0]
        v = j.split('=')[1]
        com = '"' + k + '"' + ':' + '"' + v + '"'
        list_b.append(com)
    #print(list_b)

    str_para = ''
    for i in list_b:
        #print(i)
        str_para  = str_para +i + ','

    real_para = str_para[:-1]
    print(real_para)

    return real_para


trans()