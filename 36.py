t=int(input('有幾筆測試資料：'))
v=[]

for i in range(1,t+1):
    for a in range(0,4):
        cc=int(input(''))
        v.insert(a,cc)
    if v[0]/v[1]==v[1]/v[2]==v[2]/v[3]:
        v.insert(4,int(v[3]/v[2]*v[3]))
        for s in range(0,5):
            print(v[s],end=' ')
        print()
        print('此為等比數列')
    elif v[0]-v[1]==v[1]-v[2]==v[2]-v[3]:
        v.insert(4,v[3]+v[3]-v[2])
        for s in range(0,5):
            print(v[s],end=' ')
        print()
        print('此為等差數列')
    else:
        for s in range(0,4):
            print(v[s],end=' ')
        print()
        print('輸入錯誤')