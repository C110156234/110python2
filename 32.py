a=int(input('小名有多少錢：'))
canbuy=0
price=[]
series=int((input('販賣機有幾種飲料')))
for i in range(series):
    price.append(int(input('輸入價錢')))
    if a>=int(price[i]):
        canbuy+=1
print(canbuy)