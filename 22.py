x = int(input("輸入查詢組數N為："))
a = ["123","456","789","336","775","566"]
b = ["456","789","888","558","666","221"]
c = ["9000","5000","6000","10000","12000","7000"]
for i in range(x):
    account,password=input("帳號及密碼：").split()
    if account in a:
        try: 
            if password == b[a.index(account)]:
                print(c[a.index(account)])
        except:
            print("error")
    else:
        print("error")