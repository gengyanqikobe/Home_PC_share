
list_a = []

sta = False

for i in range(0,5):
    #print(i)
    a = int(input("请输入0到13的整数："))

    if int(a) >13 or int(a) < 0:
        print('wrong number!!!')
        break
    else:
        list_a.append(a)
        sta = True



def card_continues(cards):
    if  len(cards)< 5:
        return False
    cards.sort()
    #print(cards)
    zeros = cards.count(0)
    gaps = 0
    small = zeros

    big = zeros + 1
    while big < len(cards):
       if cards[small] == cards[big]:
           print("有重复",cards[small],cards[big])
           return False
       gaps += cards[big] - cards[small] -1
       #print(gaps)
       small = big
       big = big + 1
    if gaps <= zeros:
        return "这是一个顺子",cards




#print(len(list_a))
if sta ==True:
    try:
        print(card_continues(list_a))
    except :

        print("请从新输入")
