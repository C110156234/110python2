N1 = int(input("請輸入第一個正整數："))
N2 = list(map(int,input("請輸入第二行數列中的數字：").split(' ')))
A = 0
A2 = 0
for i in N2:
    if N1 == i:
        A += 1
for i in N2:
    for j in N2:
        if i == j:
            A2 +=1
print("出現次數為:",A)