#H24121133 統計一 陳星宇
import random
lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = lst[random.randint(0,25)]
cnt = 0
his = ['d','h','l','p','t','x','z']
hiscount = [0,0,0,0,0,0,0]
def countt(ch): #算Histogram
    global his
    global hiscount
    cur = 0
    for c in his:
        if(ch <= c):
            hiscount[cur] += 1
            return
        cur = cur + 1
while(1): #input
    x = str(input('Guess the lowercase alphabet: '))
    cnt = cnt + 1
    if(x < 'a' or x > 'z' or len(x) > 1):
        print('Please enter a lowercase alphabet')
        cnt = cnt - 1
        continue
    if(x < ans):
        print('The alphabet you are looking for is alphabetically higher.')
        countt(x)
    elif(x > ans):
        print('The alphabet you are looking for is alphabetically lower.')
        countt(x)
    else:
        countt(x)
        print('Congratulations! You guessed the alphabet \"' + ans + '\" in' , cnt , "tries.")
        break
print('')#Output
print('Guess Histogram:')
print('a - d: ', '*' * hiscount[0])
print('e - h: ', '*' * hiscount[1])
print('i - l: ', '*' * hiscount[2])
print('m - p: ', '*' * hiscount[3])
print('q - t: ', '*' * hiscount[4])
print('u - x: ', '*' * hiscount[5])
print('y - z: ', '*' * hiscount[6])

