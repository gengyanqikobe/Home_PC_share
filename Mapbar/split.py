import os
sentence = 'i am laker fans,it\'s is my hornr ,once laker ,always laker'
print(sentence)
print(sentence.split(',',4)[1])
print(sentence.split(' '))

u1,u2,u3,u4 = sentence.split(',',3)#根据'，'分成4份
print('%s\n%s\n%s\n'%(u1,u2,u3))#重点！！！！！！！！！！输出多个变量
print('\n')

print('分割线-----------------------------------------------')

sentence1 = '''say
hello
my
baby'''
print(sentence1)#输出中有换行

print(sentence1.split('\n'))#去掉换行符


u1,u2,u3,u4 = sentence1.split()
print('%s %s %s %s'%(u1,u2,u3,u4))


print('分割线-----------------------------------------------')#分离路径和文件名
print(os.path.split('http://www.jb51.net/article/63592.htm')) #需要先import os
u1,u2 = os.path.split('http://www.jb51.net/article/63592.htm')
print('路径是:%s,文件名是:%s'%(u1,u2))

web = 'hello bai<[www.baidu.com]>du bye'
print(web.split('[')[1].split(']')[0])#从一段话中找到自己要的网址
