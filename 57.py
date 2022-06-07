dict1 = {'1A':127,'1B':140,'2A':117,'2B':130,'3A':137,'3B':150,'4A':99,'4B':112,'5A':115,'5B':128}
x = input("請選擇主餐及升級的套餐：")
y = input("是否升級成大杯飲料：")
z = input("是否換成大薯：")
a = dict1.get(x)
if x in dict1:
    x1 = a 
if y == '是':
    y1 =+ int(7)
elif y == '否':
    y1 =+ 0
if z == '是':
    z1 =+ int(13)
elif z == '否':
    z1 =+ 0
p = x1 + y1 + z1
print(p)