import math
#用来模拟车好卖购车计算器
def quankuan(price_car):
    price_zhekou = 0
    price_proportion = 0
    type_zhekou = int(input("请选择折扣种类，输入1选择价格优惠，输入2选择折扣优惠，没有优惠输入0:\n"))
    if type_zhekou ==1:
        price_zhekou = int(input("请输入优惠价格：\n"))
        price_car_bargain = (price_car-price_zhekou)
    elif type_zhekou ==2:
        price_proportion =int(input("请输入优惠折扣：\n"))
        price_car_bargain = round(price_car*(100-price_proportion)/100)
    else:
        print("没有优惠:\n")
        price_car_bargain = price_car
    total = price_car_bargain+800+1200+(price_car_bargain/1.17*0.1)+1230+((1270+(price_car_bargain*0.0095+285))*1.2+(120+price_car_bargain*0.0049)+price_car_bargain*0.0019+price_car_bargain*0.0015+(price_car_bargain*0.0095+285)*0.05+570+20000*0.0042+20000*3*0.0027)
    print("总花费为：%d,"%round(total))


#quankuan(30800)

def daikuan(price_car):
    price_zhekou = 0
    price_proportion = 0
    frist_proportion_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
    year_list = [1,2,3,4]
    proportion_list = []
    type_zhekou = int(input("请选择折扣种类，输入1选择价格优惠，输入2选择折扣优惠，没有优惠输入0:\n"))
    if type_zhekou ==1:
        price_zhekou = int(input("请输入优惠价格：\n"))
        price_car_bargain = (price_car-price_zhekou)
    elif type_zhekou ==2:
        price_proportion =int(input("请输入优惠折扣：\n"))
        price_car_bargain = (price_car*(100-price_proportion)/100)
        print(price_car_bargain)
    else:
        print("没有优惠:\n")
        price_car_bargain = price_car

    insurance  = math.ceil((1270+(price_car_bargain*0.0095+285))*1.2+(120+price_car_bargain*0.0049)+price_car_bargain*0.0019+price_car_bargain*0.0015+(price_car_bargain*0.0095+285)*0.05+570+20000*0.0042+20000*3*0.0027)
    print(insurance)
    buy_tax = math.ceil(price_car_bargain/1.17*0.1)
    print(buy_tax)
    necessity = 800+1200+(buy_tax)+1230+(insurance)
    print(necessity)
    for a in year_list:
        for b in frist_proportion_list:
            if a ==1:
                proportion = 0.003625
            else:
                proportion = 0.00395833
            month_pay = math.ceil((price_car_bargain*(1 - b)*proportion*((1+proportion)**(a*12)))/((1+proportion)**(a*12)-1))
            frist_pay = price_car_bargain*b +necessity
            total = necessity + month_pay*a*12 + price_car_bargain*b
                   # month_cost  = ((base_price*(1-proportion)*month*((1+month)**(year*12)))/((1+month)**(year*12) -1))
            pay_for_nothing = month_pay*12*a -price_car_bargain*(1-b)

            print("%d年首付比例为%f首付为%d月供为%d预计总花费为%d利息为%d"%(a,b,(frist_pay),(month_pay),(total),(pay_for_nothing)))
daikuan(36800)
