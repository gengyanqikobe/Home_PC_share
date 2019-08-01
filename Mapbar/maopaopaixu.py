

list_a = [3,2,7,2,10,5,27,3,32,22]
def maopao(list_a):
    for i in range(len(list_a) - 1):
        for j in range(len(list_a) - 1 - i):
            if list_a[j] < list_a[j + 1]:
                temp = list_a[j]
                list_a[j] = list_a[j + 1]
                list_a[j + 1] = temp
    return list_a

#print(maopao(list_a))

def insertpaixu(n):
    for i in range(1,len(n)):
        j = i -1
        if n[i] > n[j]:
            temp = n[i]
            n[i] = n[j]
            j = j-1
            while j>= 0 and temp >n[j]:
                n[j+1] = n[j]
                j =j-1
                print("j=",j)
            n[j+1] =temp
    return n
print(insertpaixu(list_a))




