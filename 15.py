a = list(input("輸入一組四位數字："))
for i in range(len(a)):
    a[i] = str((int(a[i])+7)%10)
b = a[0]
a[0] = a[2]
a[2] = b
c = a[1]
a[1] = a[3]
a[3] = c
h = ""
for i in range(len(a)):
    h += a[i]
print("輸出加密後的數字為：%s"%(h))