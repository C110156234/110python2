c = int(input("國文："))
e = int(input("英文："))
m = int(input("微積分："))
p = int(input("體育："))
d = int(input("程式設計："))
avg1 = (c+e+m+p+d) / 5
print("平均分數為%.2f" %(avg1))
list1 = [c,e,m,p,d]
max_value = None
for i in list1:
    if (max_value is None or i > max_value):
        max_value = i
min_value = None
for i in list1:
    if (min_value is None or i < min_value):
        min_value = i
print("平均分數:",avg1)
print("最高分科目:",max_value,"分")
print("最低分科目:",min_value,"分")