#H24121133 統計一 陳星宇
lst = list(map(int,input('Input sequence of seats: ').split()))
mx = max(lst)
n = len(lst)
sum = 0
#逐行掃
for i in range(1,mx + 1):
    dp = []
    for j in range(n):
        if(lst[j] >= i):
            dp.append(j)
    for j in range(1,len(dp)):
        sum = sum + (dp[j] - dp[j - 1] - 1)
print('Water: ',sum)
