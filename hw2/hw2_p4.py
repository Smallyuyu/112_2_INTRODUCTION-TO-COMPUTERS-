#H24121133 統計一 陳星宇
layers = int(input('Enter the number of layers (2 to 5) = '))
sl = int(input('Enter the side length of the top layer = '))
gl = int(input('Enter the growth of each layer = '))
tw = int(input('Enter the trunk width (odd number, 3 to 9) = '))
th = int(input('Enter the trunk heigh (4 to 10) = '))
top_bottom = sl * 2 - 1 #頂層三角形的底邊長
bottom_bottom = top_bottom + gl * 2 * (layers - 1) #底層三角形的底邊長
middle = (bottom_bottom // 2) + 1 #中心點
#印葉子
for i in range(0,layers):
    if(i == 0):
        print((middle - 1)* ' ' + '#')
    for j in range(3,top_bottom + gl * 2 * i + 1,2):
        left = (j // 2) + 1
        if(j == top_bottom + gl * 2 * i):
            print((middle - left) * ' ' + '#' + (j - 2) * '#' + '#')
        else:
            print((middle - left) * ' ' + '#' + (j - 2) * '@' + '#')       
#印樹幹
left = (tw // 2) + 1
for i in range(0,th):
    print((middle - left) * ' ' + tw * '|')
