x = input("輸入一整數序列為：").split()
z = []
a = ""
for i in range(len(x)):
    y=0
    if x.count(x[i])>len(x)/2 and x[i] not in z:
        z.append(x[i])
for x in range(len(z)):
    a += z[x]
if a =="":
    print("過半元素為:NO")
else:
    print("過半元素為",a)