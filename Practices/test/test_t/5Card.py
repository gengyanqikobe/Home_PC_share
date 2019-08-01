

card = []
joker_number = 0


for i in range(0,5):
    #print(i)

    a = input("pls input 1--13 or J ,j:")
    if a == 'j' or a=='J':
        print('have a joker:',a)
        joker_number = joker_number + 1
    elif int(a) >13 or int(a) < 1:
        print('wrong number!!!')
        break
    else:
        card.append(a)


#card = ['1','3','2','4']
#joker_number = 1

#print(type(card[1]),card,joker_number,)

#m冒泡排序，把得到的除了Jj外的数字排序

for i in range(0,5-joker_number):
    for j in range(0,5-joker_number-1):
        #print(j)
        if int(card[j]) > int(card[j + 1]):
            temp = card[j]
            card[j] = card[j + 1]
            card[j + 1] = temp
print("排序后：",card)

#判断是否能构成顺子
'''
bia = 0
for i in range(0,5 - joker_number-1):
    if joker_number == 0:
        #是否连续
        if int(card[i]) + 1 == int(card[i+1]):
            bia = bia + 1
            if bia == 4:
                print("这是一个顺子：",card)
                bia = 0
        else:
            print("这不是顺子",card)
            bia = 0
    elif joker_number == 1:
        if int(card[i]) + 1 == int(card[i + 1]):
            bia = bia +1
            if bia == 3:
                print("这是一个顺子：",card)
                bia = 0

        elif int(card[i]) + 2 ==int(card[i + 1]) and :
            bia = bia +1
'''
if joker_number == 0:
    if int(card[0]) + 1 == int(card[1]):
        if int(card[1]) + 1 == int(card[2]):
            if int(card[2]) + 1 == int(card[3]):
                if int(card[3]) + 1 == int(card[4]):
                    print("这是一个顺子：",card)


elif joker_number == 1:
    if int(card[0]) + 1 == int(card[1]):
        if int(card[1]) + 1 == int(card[2]):
            if int(card[2]) + 1 == int(card[3])or int(card[2]) + 2 == int(card[3]):
                print("这是一个顺子：",card)

        elif int(card[1]) + 2 == int(card[2]):
            if int(card[2]) + 1 == int(card[3]):
                print("这是一个顺子：",card)
    elif int(card[0]) + 2 == int(card[1]):
        if int(card[1]) + 1 == int(card[2]):
            if int(card[2]) + 1 == int(card[3]):
                    print("这是一个顺子：",card)


elif joker_number == 2:
    if int(card[0]) + 1 == int(card[1]):
        if int(card[1]) + 1 == int(card[2])or int(card[1]) + 2 == int(card[2])or int(card[1]) + 3 == int(card[2]):
            print("这是一个顺子：",card)
    elif int(card[0]) + 2 == int(card[1]):
        if int(card[1]) + 1 == int(card[2])or int(card[1]) + 2 == int(card[2]):
            print("这是一个顺子：",card)

