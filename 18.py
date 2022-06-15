y = 0
x = input("輸入五張牌：").split()
for i in range(len(x)):
  if x[i] == "A":
    x[i] = 1 
  if x[i] == "J":
    x[i] = 11 
  if x[i] == "Q":
    x[i] = 12
  if x[i] == "K":
    x[i] = 13
for i in range(len(x)):
    y += int(x[i])
print(y)