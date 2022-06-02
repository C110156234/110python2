list1 =[]
while True:
    x = str(input("請輸入事項（若已無事項，請輸入end）："))
    if x == 'end':
        break
    list1.append(x)
y = len(list1)
for i in range(1,y + 1):
    print(i,"、",list1[i-1])