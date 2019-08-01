
from matplotlib.pyplot import bar

#用于区间统计失败率，需要传入区间大小，以及带有失败率的txt文档地址

def block(block_size,filename): #
    data = []
    f = open(filename,'r',encoding='utf-8')
    temp_data = f.readlines()
    for i in temp_data:
        a = i.strip('%\n')
        data.append(a)

    block_number = int(100/block_size)      #区间的个数
    block_total = []                        #区间总细信息
    block_single = []                       #每个区间的详细信息
    block_start = 0                         #单个区间开始的值
    block_value = []                        #区间里面对应的值
    block_end = 0                           #单个区间结束的值
    dict_block_value ={}


    for i in range(0,block_number):
        block_single.append(block_start)        #创建单个区间，根据区间开始的值，结束的值
        block_end = block_start + block_size
        block_single.append(block_end)

        block_start = block_end                 #给开始的值复上结束的值
        block_total.append(block_single)
        block_single = []
        block_value.append(0)
    #print(block_total,block_value)

    for dat in data:
        item = float(dat)
        for i in range(0,block_number):
            if item <= block_total[i][1] and item > block_total[i][0]:
                block_value[i] = block_value[i] + 1
    #print(block_value)

    # str_block_total =[]     #存储str格式的区间合集
    # for item in block_total:
    #     str_block_total.append(str(item))         #因为输出格式问题，不采用字典形式
    # dict_block_value = dict(zip(str_block_total,block_value))

    #print(block_total,block_value)             #返回两个列表，一个是区间，一个是区间对应的值
    return block_total,block_value



#data = block(100,'fail.txt')
