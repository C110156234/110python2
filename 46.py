a = input("金:")
b = input("銀:")
c = input("銅:")
d = input("優:")
x = input("(1)字典(2)串列:")
if x == '1':
    dict1 = {'金':a,'銀':b,"銅":c,"優":d}
    for y,z in dict1.items():
        print(y,"牌得到",z,"面")
elif x == '2':
    list1 = ['金',a,'銀',b,'銅',c,'優',d]
    for i in range(0,8,2):
        print("%s牌得到%d面" %(list1[i],int(list1[i+1])))