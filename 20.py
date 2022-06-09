x = input("組數為：")
for i in range(int(x)):
    y = input("第%d組:" % (i+1)).split()
    z =int(y[0])*250+int(y[1])*175
    print("第%s組應收費用:%s"%(i+1,z))