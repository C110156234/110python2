dict1 = {"蘋果":"紅色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
f = input("請輸入水果：")
x = dict1.get(f)
if f in dict1:
    print("%s是%s" %(f,x))