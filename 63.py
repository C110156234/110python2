n=int(input('請輸入正整數n：'))
a=0
for i in range(n):
    if n%(i+1) == 0:
        a+=i+1
a-=n
if a == n:
    print('perfect')
elif a>n:
    print('abundant')
else:
    print('deficient')