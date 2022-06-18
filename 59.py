
cash=int(input('輸入金額：'))
a=cash//100
b=(cash-(a*100))//50
c=(cash-a*100-b*50)//10
d=(cash-a*100-b*50-c*10)//5
e=(cash-a*100-b*50-c*10-d*5)
print(a+b+c+d+e)