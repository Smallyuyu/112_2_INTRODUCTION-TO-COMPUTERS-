n = int(input('Enter the size of the grid: '))
arr = [['_'] * n for i in range(n)]
def printmap():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end = ' ')
        print('')
printmap()
while(1):
    op = str(input(('Enter the cell coordinates to edit: ')))
    if(op == 'done'):
        break
    x,y = op.split(',')
    ch = str(input('Enter the new value for the cell: '))
    arr[int(x)][int(y)] = ch
    printmap()
