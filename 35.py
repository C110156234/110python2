a = input('第一行輸入字串sA：')
b = input('第二行輸入字串sB：').split(' ')
for i in range(0,len(b)):
    if a==b[i]:
        print('子字串判斷為: Yes')