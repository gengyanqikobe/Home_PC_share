import matplotlib.pyplot as plt
import numpy as np

from Practices.test.test_Matplotlib import block


def bar_graph(block_number,block_total,block_value):

    #创建一个10x10的窗口,分辨率80
    plt.figure(figsize=(10,10),dpi=80)

    #再创建一个1x1子图
    plt.subplot(1,1,1)

    #柱子数
    N =block_number
    #对应的值
    values = block_value

    #包含每个柱子下标的序列
    index = np.arange(N)

    #柱子宽度
    width = 0.35

    #绘制柱状图，每个柱子为紫罗兰色
    p2 = plt.bar(index,values,width,label='test',color = "#87CEFA")

    #设置横轴标签
    plt.xlabel("months")
    #y轴
    plt.ylabel("cost")

    #添加标题
    plt.title("每月话费")

    #横坐标刻度
    plt.xticks(index,(block_total))
    #纵坐标刻度
    plt.yticks(np.arange(0,1000,50))

    #添加图例
    plt.legend(loc="upper right")

    plt.show()


result = block(20,'fail.txt')
block_number = result[0]
block_total = result[1]
block_value = result[2]
print(block_number,block_total,block_value)
bar_graph(block_number,block_total,block_value)