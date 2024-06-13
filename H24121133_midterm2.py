import random
#H24121133 統計一 陳星宇
#用random的方式來選擇要走哪個方向 用來找路徑
#input
n = int(input('Enter the number of rows (N): '))
m = int(input('Enter the number of columns (M): '))
board = [[' '] * m for i in range(n)]
max_obs = n * m - (n + m - 1)
obs_list = []
path_list = []
obs = int(input("Enter the number of obstacles (0-" + str(max_obs) + "): "))
#防呆
while(obs > 42 or obs > max_obs or obs < 0):
    obs = int(input("Re-enter again (0-" + str(max_obs) + "): "))

#找路徑
def generate_path(n,m):
    global board
    global path_list
    x = 0
    y = 0
    path_list.append(0)
    for i in range(1,n + m - 1):
        op = random.randint(0,1)
        if(op == 0):
            x = x + 1
            if(x >= n):
                x = x - 1
                y = y + 1
        else:
            y = y + 1
            if(y >= m):
                y = y - 1
                x = x + 1
        path_list.append(x * m + y)

#加障礙物    
def add_obstacles(maze,obs):
    global obs_list
    global board
    global path_list
    global n,m
    cnt = 0
    while(cnt < obs):
        x = random.randint(0,n * m - 1)
        if(x in obs_list or x in path_list):
            continue
        obs_list.append(x)
        cnt = cnt + 1
    for i in range(obs):
        board[obs_list[i] // m][obs_list[i] % m] = 'X'

#產迷宮
def generate_maze(n,m):
    global obs
    maze = generate_path(n,m)
    maze = add_obstacles(maze,obs)

#print迷宮
def print_maze(maze):
    print('Generated Maze Map:')
    global n,m
    col = "+" + "---+" * m
    print(col)
    for i in range(n):
        print('|',end = '')
        for j in range(m):
            if(board[i][j] == 'X'):
                print(' X |',end = '')
            else:
                print('   |',end = '')
        print('')
        print(col)
#start
maze = generate_maze(n,m)
print_maze(maze)
