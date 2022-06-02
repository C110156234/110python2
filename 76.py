while True:
    x = input('傳送密碼(6位數)')
    if len(x) ==6:
        for i in range(len(x)):
          print(int(x[i])*4%7,end='')
        break
    else:
        print('請輸入6位數')