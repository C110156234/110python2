x = input("輸入值為：")
y = x.split(",")
z = sorted(y)
a = sorted(y , reverse=True)
b1 = ""
b2 = ""
for i in range(len(y)):
    b1 += a[i]
    b2 += z[i]
print("最大值數列與最小值數列差值為：%s"%(int(b1)-int(b2)))