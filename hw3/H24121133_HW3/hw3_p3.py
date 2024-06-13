#H24121133 統計一 陳星宇
#變數
board = [['-'] * 7 for i in range(6)]
curplayer = 0
topN = [0 for i in range(7)]
PlayerToChar = ['X','O']
remains = 42
global xn,yn
#印地圖
def printmap():
    for i in range(0,6):
        print('+---+---+---+---+---+---+---+')
        for j in range(0,7):
            print('| ' + board[i][j] + ' ',end = '')
        print('|')
    print('+---+---+---+---+---+---+---+')
    print('  0   1   2   3   4   5   6')
    print('')
    
#輸入狀況排除
def Error(n):
    if(n.isdigit()):
        n = int(n)
        if(n >= 0 and n <= 6):
            if(topN[n] < 6):
                return 0
            print('The column is full. Try another column.')
            return 1
        else:
            print('Out of range,try again [0-6].')
            return 1
    else:
        print('Invalid input, try again [0-6].')
        return 1

#遊戲結束
#若新增了某個點導致獲勝者產出，則該點必在獲勝條件之線上
def end(c,x,y):
    left,right,top,bottom,d1,d2,d3,d4,flag1,flag2,flag3,flag4 = y,y,x,x,0,0,0,0,0,0,0,0
    #Setting
    #左右
    while(left >= 0 and board[x][left] == c):
        left = left - 1
    while(right < 7 and board[x][right] == c):
        right = right + 1
    #上下
    while(top >= 0 and board[top][y] == c):
        top = top - 1
    while(bottom < 6 and board[bottom][y] == c):
        bottom = bottom + 1
    #左下右上斜線(偏移量)
    while(x + d1 < 6 and y - d1 >= 0 and board[x + d1][y - d1] == c):
        d1 = d1 + 1
    while(x - d2 >= 0 and y + d2 < 7 and board[x - d2][y + d2] == c):
        d2 = d2 + 1
    #左上右下斜線
    while(x + d3 < 6 and y + d3 < 7 and board[x + d3][y + d3] == c):
        d3 = d3 + 1
    while(x - d4 >= 0 and y - d4 >= 0 and board[x - d4][y - d4] == c):
        d4 = d4 + 1
    #判斷
    if((right - left - (right != y and left != y)) >= 4):
        for i in range(left + 1,right):
            board[x][i] = c.lower()
        flag1 = 1
    if((bottom - top - (bottom != x and top != x)) >= 4):
        for i in range(top + 1,bottom):
            board[i][y] = c.lower()
        flag2 = 1
    if(d1 + d2 - (d1 != 0 and d2 != 0) >= 4):
        for i in range(-d1 + 1,d2):
            board[x - i][y + i] = c.lower()
        flag3 = 1
    if(d3 + d4 - (d3 != 0 and d4 != 0) >= 4):
        for i in range(-d3 + 1,d4):
            board[x + i][y + i] = c.lower()
        flag4 = 1
    if(flag1 or flag2 or flag3 or flag4):
        return 1
    return 0
#main
while(1):
    printmap()
    num = str(input('Player ' + PlayerToChar[curplayer] + ' >> '))
    while(Error(num)):
        num = str(input('Player ' + PlayerToChar[curplayer] + ' >> '))
    num = int(num)
    board[5 - topN[num]][num] = PlayerToChar[curplayer]
    topN[num] += 1
    remains -= 1
    x = num
    y = 6 - topN[num]
    if(end(PlayerToChar[curplayer],y,x)):
        printmap()
        print('Winner: ',PlayerToChar[curplayer])
        break
    if(remains == 0):
        print('Draw')
        break
    curplayer = curplayer ^ 1
