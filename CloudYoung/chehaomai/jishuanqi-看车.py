import  math



#）：月供金额= [裸车价*(1-首付比例)*月利率*(1+月利率)^还款月数]/[(1+月利率)^还款月数-1
def month_cost():
    year = int(input("请输入贷款年限："))
    #proportion = float(input("请输入首付比例，如：0.3,0.2等："))
    base_price = int(input("请输入裸车价："))

    proportion_all_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]

    if year == 1:
     month = 0.003625
    elif year == 2:
     month = 0.003958
    elif year ==3:
        month = 0.003958
    else:
        print("年限错误")
    for proportion in proportion_all_list:

        month_cost  = ((base_price*(1-proportion)*month*((1+month)**(year*12)))/((1+month)**(year*12) -1))

        print("首付为%.2f,每月月供为%d："%(proportion,round(month_cost)))
month_cost()
