x = int(input("請輸入階乘值M："))
y = 0
z = 1
while x > z:
    y += 1
    z *= y
print("超過M為1000的最小階層N值為:",y)