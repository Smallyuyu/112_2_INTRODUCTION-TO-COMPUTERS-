import random
import time
charmap = [[''] * 9 for i in range(9)]
vismap = [[0] * 9 for i in range(9)]
intmap = [[0] * 9 for i in range(9)]
lst = ['a','b','c','d','e','f','g','h','i']
bomb = []
for i in range(0,81):
    bomb.append(i)
remains = 10
startgame = 0
endgame = 0
t1 = time.time()
#Bomb: intmap = -1
#Flag: vismap = 2
def printcolumn(s):
    if(s == 'null'):
        print('   +---+---+---+---+---+---+---+---+---+')
    else:
        print(' ' + s + ' |',end = '')
        if(startgame == 0 and endgame == 1):
            for i in range(9):
                if(intmap[int(s) - 1][i] == -1):
                    print(' ' + 'X' + ' |',end = '')
                else:
                    print(' ' + chr(intmap[int(s) - 1][i] + ord('0')) + ' |',end = '')
        else:
            for i in range(9):
                if(vismap[int(s) - 1][i] == 1):
                    print(' ' + chr(intmap[int(s) - 1][i] + ord('0')) + ' |',end = '')
                elif(vismap[int(s) - 1][i] == 2):
                    print(' ' + 'F' + ' |',end = '')
                elif(vismap[int(s) - 1][i] == 0):
                    print('   |',end = '')
                elif(vismap[int(s) - 1][i] == -1):
                     if(endgame == 1):
                         print(' ' + 'X' + ' |',end = '')
        print('')
        
def printmap():
    print('     ',end = '')
    for i in lst:
        print(i,end = '   ')
    print('')
    for i in range(1,10):
        printcolumn('null')
        printcolumn(str(i))
    printcolumn('null')
    
def dfs(x,y):
    if(x >= 0 and y >= 0 and x < 9 and y < 9):
        if(vismap[x][y] >= 1):
            return
        if(intmap[x][y] == -1):
            return
        vismap[x][y] = 1
        if(intmap[x][y] == 0):
            dfs(x + 1,y)
            dfs(x - 1,y)
            dfs(x,y + 1)
            dfs(x,y - 1)

def rndgame(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            tx = x + i
            ty = y + j
            if(tx >= 0 and ty >= 0 and tx < 9 and ty < 9):
                bomb.remove(tx * 9 + ty)
    random.shuffle(bomb)
    for i in range(0,10):
        intmap[int(bomb[i] / 9)][int(bomb[i] % 9)] = -1
    for i in range(-1,2):
        for j in range(-1,2):
            tx = x + i
            ty = y + j
            if(tx >= 0 and ty >= 0 and tx < 9 and ty < 9):
                bomb.append(tx * 9 + ty)
    
def point(s):
    return int(s[1]) - 1,ord(s[0]) - ord('a')

def help():
    print('Enter the column followed by the row (ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f).Type \'help\' to show this message again')
    print('')
    
def error():
    print('Invalid cell. Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex:a5f).')
    print('')

def judge(o):
    if(o[0] >= 'a' and o[0] <= 'i' and o[1] >= '1' and o[1] <= '9'):
        return 1
    return -1

def game(op):
    if(len(op) == 2):
        if(judge(op) == -1):
            error()
            return -1
        n,m = point(op)
        if(vismap[n][m] == 1):
            print('That cell is already shown.')
            return -1
        elif(vismap[n][m] == 2):
            print('There is a flag there.')
            return -1
        else:
            global startgame
            if(startgame == 0):
                startgame = 1
                rndgame(n,m)
                Dovaluemap()
                global t1
                t1 = time.time()
            if(intmap[n][m] == -1):
                return -2
            dfs(n,m)
    elif(len(op) == 3 and op[2] == 'f'):
        if(judge(op) == -1):
            error()
            return -1
        global remains
        n,m = point(op)
        if(vismap[n][m] == 1):
            print('Cannot put a flag there.')
            return -1
        if(vismap[n][m] == 2):
            vismap[n][m] = 0
            if(intmap[n][m] == -1):
                remains = remains + 1
        else:
            vismap[n][m] = 2
            if(intmap[n][m] == -1):
                remains = remains - 1
    else:
        error()
        return -1
    return 1
                
def loop():
    while(1):
        yn = str(input(('Play again? (y/n): ')))
        if(yn == 'y'):
            return 1
        elif(yn == 'n'):
            return -1

def init():
    global remains,charmap,vismap,intmap,startgame,endgame
    remains = 10
    charmap = [[''] * 9 for i in range(9)]
    vismap = [[0] * 9 for i in range(9)]
    intmap = [[0] * 9 for i in range(9)]
    Dovaluemap()
    startgame = 0
    endgame = 0
    printmap()
    help()
printmap()
help()

def Dovaluemap():
    for i in range(0,9):
        for j in range(0,9):
            if(intmap[i][j] == -1):
                continue
            cnt = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    tx = i + k
                    ty = j + l
                    if(tx >= 0 and ty >= 0 and tx < 9 and ty < 9):
                        if(intmap[tx][ty] == -1):
                            cnt = cnt + 1
            intmap[i][j] = cnt
while(1):
    print('Enter the cell (',remains,'mines left):',end = ' ')
    op = str(input())
    v = game(op)
    if(v == -1):
        continue
    if(v == -2):
        endgame = 1
        startgame = 0
        print('Game Over')
        printmap()
        if(loop() == -1):
            break
        else:
            init()
            continue
    if(remains == 0):
        endgame = 1
        startgame = 0
        t2 = time.time()
        delta = int(t2 - t1)
        print('You Win. It took you %d minutes and %d seconds.' % (delta / 60,delta % 60))
        printmap()
        if(loop() == -1):
            break
        else:
            init()
            continue
    printmap()

    
