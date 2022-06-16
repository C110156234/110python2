a = str(input("輸入甲方的數字："))
b = str(input("輸入乙方的數字："))
c = len(a)
d=[]

for i in range(0 , c-1):
    if int(a[i]) > int(b[i]):
        d.append("贏")
    elif int(a[i]) < int(b[i]):
        d.append("輸")
    elif int(a[i]) == int(b[i]):
        d.append("和")

print(d)