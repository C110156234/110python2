a = int(input("輸入一個度數(正整數)："))
if a <= 120:
    print("summer month：%.2f" %(a*2.1))
    print("not-summer month：%.2f" %(a*2.1))
elif 120 < a and a <= 330:
    print("summer month：%.2f" %((a-120)*3.02 + 120*2.1))
    print("not-summer month：%.2f" %((a-120)*2.68 + 120*2.1))
elif 330 < a and a <= 500:
    print("summer month：%.2f" %(120 * 2.1 + 210 * 3.02 + ((a-330)*4.39)))
    print("not-summer month：%.2f" %(120 * 2.1 + 210 * 2.68 + ((a-330)*3.61)))
elif 500 < a and a <= 700:
    print("summer month：%.2f" %(120 * 2.1 + 210 * 3.02 + 170 * 4.39 +((a - 500)*4.97)))
    print("not-summer month：%.2f" %(120 * 2.1 + 210 * 2.68 + 170 * 3.61 +((a - 500)*4.01)))
elif a > 700:
    print("summer month：%.2f" %(120 * 2.1 + 210 * 3.02 + 170 * 4.39 + 200 * 4.97 +((a - 700)*5.63)))
    print("not-summer month：%.2f" %(120 * 2.1 + 210 * 2.68 + 170 * 3.61 + 200 * 4.01 +((a - 700)*4.5)))