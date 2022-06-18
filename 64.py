a1=int(input('請輸入第一個要判斷的數字：'))
a2=int(input('請輸入第二個要判斷的數字：'))
aa=[]
for k in range(99):
    if k > 1:
        for i in range(2, int(k/2)+1):
            if (k % i) == 0:
                break
        else:
            aa.append(k)
if aa.count(a1)!=0 and aa.count(a2)!=0:
    if a2-a1==2:
        print('Y')
    else:
        print('N')
else:
    print('N')