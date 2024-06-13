#H24121133 統計一 陳星宇
import csv
file = csv.reader(open("nba_standings.csv"))
data = []
for row in file:
    data.append(row)
del data[0]
n = len(data)
n = n - 1
def question1():
    print('Question 1 :')
    global data
    global n
    for i in range(n):
        if(data[i][0] == "Eastern"):
            w = data[i][2].split('-')
            w1 = int(w[0])
            w2 = int(w[1])
            a = data[i][8].split('-')
            a1 = int(a[0])
            a2 = int(a[1])
            h1 = w1 - a1
            h2 = w2 - a2
            aa = a1 / (a1 + a2)
            hh = h1 / (h1 + h2)
            if(aa > hh):
                print(data[i][1])
def question2():
    print('Question 2 :')
    global data
    global n
    s1 = 0
    s2 = 0
    c1 = 0
    c2 = 0
    for i in range(n):
        if(data[i][0] == "Eastern"):
            s1 = s1 + float(data[i][5]) - float(data[i][6])
            c1 = c1 + 1
        else:
            s2 = s2 + float(data[i][5]) - float(data[i][6])
            c2 = c2 + 1
    if(s1 / c1 > s2 / c2):
        print('Eastern')
    else:
        print('Western')
def question3():
    print('Question 3 :')
    global data
    global n
    for i in range(n):
        for j in range(i + 1,n):
            if(data[i][3] < data[j][3]):
                data[i],data[j] = data[j],data[i]
    for i in range(n):
        print(data[i][1])
question1()
print('')
question2()
print('')
question3()
    
