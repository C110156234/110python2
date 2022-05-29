a=[]
for i in range(10):
    a.append(int(input("輸入%d個數字:" %(i+1))))
a.sort(reverse=True)
print("最大3數:%d,%d,%d" %(a[0],a[1],a[2]))
a.sort()
print("最小3數:%d,%d,%d" %(a[0],a[1],a[2]))