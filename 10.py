x , y = map(int,input("輸入N M的值:").split())
list1=list(map(int,input("輸入矩陣第1列為:").split()))
list2=list(map(int,input("輸入矩陣第2列數值為:").split()))
for i in range(x):
    for n in range(y):
        print(f"輸出矩陣數值第{n + 1}列:{list1[n]} {list2[n]}")
    break