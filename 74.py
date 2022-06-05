a = ['red','blue','red','green']
n = 9
for i in range(10):
    x = input("依序輸入四種顏色(中間以空白間隔):")
    y = x.split()
    t = ""
    if len(y) == 4:
        for z in range(4):
            if y[z] == a[z]:
                t += '1'
            elif y[z] in a:
                t += '2'
            else:
                t += '3'
        print(t)
        if t == '1111':
            print("正確答案")
            break
        else:
            print("你還有%d次機會" %(n))
            n -= 1
    else:
        print("請輸入正確")
    if n == -1:
        print("挑戰失敗")