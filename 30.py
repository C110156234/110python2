ans=input('輸入答案(四位數)：')
num=input('輸入猜數(四位數)：')
if num=='0':
    print('end')
    exit()
a=0
b=0
for i in range(4):
    if num[i]==ans[i]:
        a=a+1
    elif num[i] in ans[i]:
        b=b+1
print("%dA %dB" %(a,b))  