#H24121133 統計一 陳星宇
x,y,k = map(int,input('Enter index x,y,k (seperated by whitespace): ').split())
print('Enter the matrix by multiple lines: ')
lst = list(map(int,input().split()))
n = len(lst)
vis = [[0] * n for i in range(n)]
arr = []
arr.append(lst)
for i in range(0,n - 1,1):
    lst = list(map(int,input().split()))
    arr.append(lst)
num = arr[x][y]
def dfs(a,b):
    if(a < 0 or b < 0 or a >= n or b >= n):
        return
    if(vis[a][b] or arr[a][b] != num):
        return
    vis[a][b] = 1
    arr[a][b] = k
    dfs(a,b + 1)
    dfs(a,b - 1)
    dfs(a + 1,b)
    dfs(a - 1,b)
dfs(x,y)
print('q')
for i in range(n):
    for j in range(n):
        print(arr[i][j],end = ' ')
    print('')
