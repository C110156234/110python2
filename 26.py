while True:
    x = input('檢測的字串(end 結束)：')
    if x != 'end':
         y = input('檢測的單一字元')
         print('字元%s出現次數為:%d'%(y,x.count(y)))
    else:
        print('檢測結束')
        break