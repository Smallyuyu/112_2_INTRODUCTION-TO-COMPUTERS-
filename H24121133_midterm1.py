k = 3
while(k > 0):
    #i * j
    i = 9
    while(i >= 1):
        j = k * 3
        while(j >= (k * 3) - 2):
            print(i,' x ',j,' = ', end = '')
            print("%-2d" % (i * j),end = '   ') #向左對齊
            j = j - 1
        print('') #換行
        i = i - 1
    if(k != 1): #最後一個不用換行
        print('') #換行
    k = k - 1
