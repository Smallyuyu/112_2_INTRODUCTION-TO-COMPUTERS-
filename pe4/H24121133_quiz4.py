#H24121133 統計一 陳星宇
#用dp找lcs然後記錄前一個接的數字 在遍歷印出
st = str(input('Enter a sequence of integers separeted by whitespace: '))
num = []
num = st.split(' ')
n = len(num)
linklist = [-1] * n
dp = [1] * n
for i in range(0,n):
    for j in range(0,i):
        if(int(num[i]) > int(num[j])):
            if(dp[j] + 1 > dp[i]):
                linklist[i] = j
                dp[i] = dp[j] + 1
ans = 1
lastele = -1
for i in range(0,n):
    if(dp[i] > ans):
        lastele = i
        ans = dp[i]
anss = []
while(linklist[lastele] != -1):
    anss.append(num[lastele])
    lastele = linklist[lastele]
anss.append(num[lastele])
print('Length:',ans)
print('LICS: [',end = '')
n = len(anss)
if(n == 1):
    print(int(anss[n - 1]),']')
else:
    print(int(anss[n - 1]),end = '')
    for i in range(1,n):
        print(', ',int(anss[n - i - 1]),end = '')
    print(']')
#print(anss)
