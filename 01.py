def is_prime(n):
    for i in range(2, n):
        if n % i == 0:  
            return False
    if n == 1:
        return False
    return True     
user = input('請輸入正整數：')
num=[]
for i in range(len(user),0,-1):
    for s in range(i):
        num.append(int(user[s:i]))
count=[]
for h in num:
    if (is_prime(h)==True):
        count.append(h)
if (len(count)>0):
    count.sort()
    count.reverse()
    print('子字串中最大的字串為：'+str(count[0]))
else:
    print('No prime found')