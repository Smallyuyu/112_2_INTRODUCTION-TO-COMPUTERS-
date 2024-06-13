#H24121133 統計一 陳星宇
n = int(input('Input the total number of students (n>0) : '))
num = []
for i in range(1,n + 1,1):
    num.append(i)
cnt = n
cur = 2
while(cnt > 1):
    if(cur >= len(num)):
        cur = cur % len(num)
    del num[cur]
    cur += 2
    cnt -= 1
print('The last ID is : ',num[0])
    
