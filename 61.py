time=input('請輸入遊戲時間(例:10:00)：').split(':')
time1=int(time[0])*60+int(time[1])
t1=time1-75
q=t1//30+1
to=6*q+q//3-q//2
print(to,'隻兵')