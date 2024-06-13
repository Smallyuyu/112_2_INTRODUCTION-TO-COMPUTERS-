#H24121133 統計一 陳星宇
import os
import keyboard
clear = lambda: os.system('cls')#清畫面
n=40#地圖大小
m=20
d = 1#方向
board = [[' '] * 40 for i in range(20)]#地圖
curx=1#當前位置
cury=3#初始長度為3所以在1,3
snake = [[1,3],[1,2],[1,1]]#蛇的初始本體位置
sp = 0#紀錄吃了幾個special,normal
nor = 0
pauseflag = 0#暫停flag
endflag = 0#遊戲結束flag
for i in range(n):#邊界
    board[0][i] = 'o'
    board[19][i] = 'o'
for i in range(m):#邊界
    board[i][0] = 'o'
    board[i][39] = 'o'
def on_key_press(event):#監聽鍵盤
    if(event.name == "w"):
        return 4
    elif event.name == 'a':
        return 3
    elif event.name == 's':
        return 2
    elif event.name == 'd':
        return 1
    elif event.name == 'space':
        return 0
def random_normal():#產生normal food
    flag = 0
    global snake
    global board
    while(1):#產生normal food
        flag = 1
        x = random.randint(1,39)
        y = random.randint(1,19)
        lst = [x,y]
        for i in range(len(snake)):#如果產生在蛇體內就重新產生
            if(snake[i] == lst):
                flag = 0
        if(flag == 1):
            board[y][x] = 'π'
            return
def random_special():#產生special
    flag = 0
    global snake
    global board
    while(1):#產生special food
        flag = 1
        x = random.randint(1,39)
        y = random.randint(1,19)
        lst = [x,y]
        for i in range(len(snake)):
            if(snake[i] == lst):#如果在蛇體內就重新產生
                flag = 0
        if(flag == 1):
            board[y][x] = 'X'
            return
    
def game():
    global d,pauseflag,endflag
    op = keyboard.on_press(on_key_press)#偵測輸入的按鍵
    if(op == 0):#按空白建暫停
        pauseflag = 1
        return
    else:#偵測按鍵方向WASD
        d = op
    global sp,nor,n,m,curx,cury
    global snake
    global board
    l = len(snake)
    last = snake[l - 1]
    if(d == 1):#向右移動
        if(board[snake[l][0],snake[1][1] + 1] == 's'):#撞到自己死掉
            endflag = 2
            return
        for i in range(l):
            snake[i][1]  = snake[i][1] + 1
    if(d == 2):#向下移動
        if(board[snake[l][0] + 1,snake[1][1]] == 's'):#撞到自己死掉
            endflag = 2
            return
        for i in range(l):
            snake[i][0] = snake[i][0] + 1
    if(d == 3):#向左移動
        if(board[snake[l][0],snake[1][1] - 1] == 's'):#撞到自己死掉
            endflag = 2
            return
        for i in range(l):
            snake[i][1] = snake[i][1] - 1
    if(d == 4):#向上移動
        if(board[snake[l][0] - 1,snake[1][1]] == 's'):#撞到自己死掉
            endflag = 2
            return
        for i in range(l):
            snake[i][0] = snake[i][0] - 1
    if(board[curx][cury] == 'π'):#normal
        nor = nor + 1
        snake.push(last)
        board[curx][cury] = ' '
        random_normal()#立即產生normal food
    if(board[curx][cury] == 'X'):#special
        if(len(snake) != 1):#長度不為1才能吃
            sp = sp + 1
            snake.pop()
        board[curx][cury] = ' '
        random_special()#立即產生special food
    for i in range(m):#清除上次的蛇體
        for j in range(n):
            if(board[i][j] == 's'):
                board[i][j] = ' '
    for i in len(snake):#印蛇
        board[snake[i][0]][snake[i][1]] = 's'
    for i in range(m):#印地圖
        for j in range(n):
            print(board[i][j],end='')
        print('')
    if(curx == 0 or cury == 0 or curx == m - 1 or cury == n - 1):#碰到邊界遊戲結束
        endflag = 1
clear()#清畫面
while(1):
    if(pauseflag == 0):
        game()
        if(endflag == 1):
            break
#結算畫面
print('normal food:',nor)
print('special food:',sp)
print('length:',len(snake))
if(endflag == 1):
    print('collides with obstacles')
elif(endflag == 2):
    print('collides with itself')
