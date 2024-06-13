#H24121133 統計一 陳星宇
def pol(s2):
    for i in range(0,len(s2),1):
        if(s2[i] == '^'):
            return int(s2[0:i]) ** (int(s2[i + 1:len(s2)]))
def cal(s1):
    if('^' not in s1):
        if('*' not in s1):
            return int(s1[(s1[0] == '+'):len(s1)])
        else:
            for i in range(0,len(s1),1):
                if(s1[i] == '*'):
                    index = i
                    break;
            return int(s1[(s1[0] == '+'):i]) * int(s1[i + 1:len(s1)])
    elif('*' in s1):
        for i in range(0,len(s1),1):
            if(s1[i] == '*'):
                index = i
                break;
        return int(s1[(s1[0] == '+'):i]) * pol(s1[i + 1:len(s1)])
    else:
        return pol(s1[(s1[0] == '+'):len(s1)])
        
s = str(input('Input polynomial: '))
x = int(input('Input the value of X: '))
left = 0
num = []
if(s[0] != '-'):
    s = '+' + s
for i in range(0,len(s),1):
    if(s[i] == '+' or s[i] == '‐' or s[i] == '-'):
        if(i == 0):
            continue
        num.append(s[left:i])
        left = i
num.append(s[left:len(s)])
sum = 0
for i in num:
    sum += cal((i.replace('X',str(x))))
print('Evaluated Result: ',sum)
