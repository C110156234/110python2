n=int(input('小狗可跑到的n個地方'))
v=[]
for i in range(0,n):
    a=int(input(''))
    if a%11==0 or a%9==0:
        print('第'+str(i+1)+'個點',a)