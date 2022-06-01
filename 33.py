c = int(input("國文："))
e = int(input("英文："))
m = int(input("微積分："))
p = int(input("體育："))
d = int(input("程式設計："))
dict1 = {c:"國文",e:"英文",m:"微積分",p:"體育",d:"程式設計"}
avg1 = (c+e+m+p+d) / 5
list1 = [c,e,m,p,d]
x = 0
for i in range(len(list1)):
    for j in range(len(list1)-1-i):
        if list1[j]<list1[j+1]:
            x = list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=x
max_value = list1[0]
min_value = list1[4]
print("平均分數為%.2f" %(avg1))
print("最高分科目:%s%d分" %(dict1[max_value],max_value))
print("最低分科目:%s%d分" %(dict1[min_value],min_value))