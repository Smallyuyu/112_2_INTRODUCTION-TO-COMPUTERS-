#H24121133 統計一 陳星宇
n = int(input("Input the range number: "))
n += 1
for i in range(2,n,2): #只有偶數有可能會是Perfect Number
    sum = 0
    for j in range(1,int(i ** 0.5) + 1): #開根號加速運算
        if(i % j == 0):
            sum += (j + int(i / j))
    if(sum / 2 == i):
        print(i)
