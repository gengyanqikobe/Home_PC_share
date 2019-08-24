


list_a = ['{"a2":"aaa"}','{"a3":"bbb"}','{"a1":"ccc"}']



dict_a={}

for i in list_a:
    #eval对str格式可以直接转换为字典
    dict_i = eval(i)
    dict_a.update(dict_i)
dict_a.update({'kkk':'afb'})
print(dict_a)

#list中sort函数的用法，没有返回值，但是会改变list本身
list_key = list(dict_a.keys())
list_key.sort(reverse=True)
print("使用sort排序后:",list_key)


#根据key值排序
#注意i取得都是key的值
for i in sorted(dict_a):
    print("按照key排序：",(i,dict_a[i]))

#根据values排序
for i in sorted(dict_a,key=dict_a.__getitem__):
    print("按照values排序：",(i,dict_a[i]))

#输入（）里面的值就找对应的，不输入就是获得所有
print(dict_a.__getitem__('kkk'))