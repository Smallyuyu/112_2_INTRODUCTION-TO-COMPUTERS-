import csv
file = csv.reader(open("IMDB-Movie-Data.csv"))
data = []
for row in file:
    data.append(row)
del data[0]
n = len(data)
def question1():
    print('Question 1 :')
    global data
    global n
    subdata = []
    for i in range(n):
        if(data[i][5] == "2016"):
            subdata.append(data[i])
    sn = len(subdata)
    for i in range(sn):
        for j in range(i + 1,sn):
            if(subdata[j][7] > subdata[i][7]):
                subdata[i][7],subdata[j][7] = subdata[j][7],subdata[i][7]
    for i in range(1,4):
        print('No.',i,subdata[i - 1][1])
    print('')
def question2():
    print('Question 2 :')
    global data
    global n
    name_lst = []
    cnt_lst = []
    for i in range(n):
        name = data[i][3]
        if(name in name_lst):
            for j in range(len(name_lst)):
                if(name == name_lst[j]):
                    cnt_lst[j] = cnt_lst[j] + 1
                    break
        else:
            name_lst.append(name)
            cnt_lst.append(1)
    ans = ""
    cnt = 0
    for i in range(len(name_lst)):
        if(cnt_lst[i] > cnt):
            cnt = cnt_lst[i]
            ans = name_lst[i]
    print(ans)
    print('')
def question3():
    print('Question 3 :')
    global data
    global n
    name_lst = []
    rev_lst = []
    for i in range(n):
        name = data[i][4]
        if(data[i][9] == ""):
            continue
        if(name in name_lst):
            for j in range(len(name_lst)):
                if(name == name_lst[j]):
                    rev_lst[j] = rev_lst[j] + float(data[i][9])
                    break
        else:
            name_lst.append(name)
            rev_lst.append(float(data[i][9]))
    ans = ""
    cnt = 0
    for i in range(len(name_lst)):
        if(rev_lst[i] > cnt):
            cnt = rev_lst[i]
            ans = name_lst[i]
    print(ans)
    print('')
def question4():
    print('Question 4 :')
    global data
    global n
    total = 0
    cnt = 0
    for i in range(n):
        name = data[i][4]
        if("Emma Watson" in name):
            total = total + float(data[i][7])
            cnt = cnt + 1
    print(total / cnt)
    print('')
def question5():
    print('Question 5 :')
    global data
    global n
    name_lst = []
    cnt_lst = []
    for i in range(n):
        name = data[i][4]
        sublst = name.split('|')
        for k in range(len(sublst)):
            name = sublst[k]
            if(name in name_lst):
                for j in range(len(name_lst)):
                    if(name == name_lst[j]):
                        cnt_lst[j] = cnt_lst[j] + 1
                        break
            else:
                name_lst.append(name)
                cnt_lst.append(1)
    for i in range(len(name_lst)):
        for j in range(i + 1,len(name_lst)):
            if(cnt_lst[j] > cnt_lst[i]):
                cnt_lst[i],cnt_lst[j] = cnt_lst[j],cnt_lst[i]
                name_lst[i],name_lst[j] = name_lst[j],name_lst[i]
    for i in range(4):
        print(i + 1,name_lst[i])
    print('')
def question6():
    print('Question 6 :')
    global data
    global n
    name_lst = []
    cnt_lst = []
    for i in range(n):
        director = data[i][3]
        name = data[i][4]
        sublst = name.split('|')
        for k in range(len(sublst)):
            name = (director,sublst[k])
            if(name in name_lst):
                for j in range(len(name_lst)):
                    if(name == name_lst[j]):
                        cnt_lst[j] = cnt_lst[j] + 1
                        break
            else:
                name_lst.append(name)
                cnt_lst.append(1)
    for i in range(len(name_lst)):
        for j in range(i + 1,len(name_lst)):
            if(cnt_lst[j] > cnt_lst[i]):
                cnt_lst[i],cnt_lst[j] = cnt_lst[j],cnt_lst[i]
                name_lst[i],name_lst[j] = name_lst[j],name_lst[i]
    for i in range(7):
        print(i + 1,name_lst[i])
    print('')
def question7():
    print('Question 7 :')
    global data
    global n
    name_lst = []
    cnt_lst = []
    for i in range(n):
        name = data[i][3]
        sublst = data[i][4].split('|')
        if(name in name_lst):
            for j in range(len(name_lst)):
                if(name == name_lst[j]):
                    cnt_lst[j] = cnt_lst[j] + len(sublst)
                    break
        else:
            name_lst.append(name)
            cnt_lst.append(len(sublst))
    for i in range(len(name_lst)):
        for j in range(i + 1,len(name_lst)):
            if(cnt_lst[j] > cnt_lst[i]):
                cnt_lst[i],cnt_lst[j] = cnt_lst[j],cnt_lst[i]
                name_lst[i],name_lst[j] = name_lst[j],name_lst[i]
    for i in range(3):
        print(i + 1,name_lst[i])
    print('')
def question8():
    print('Question 8 :')
    global data
    global n
    name_lst = []
    cnt_lst = []
    for i in range(n):
        name = data[i][3]
        sublst = data[i][2].split('|')
        if(name in name_lst):
            for j in range(len(name_lst)):
                if(name == name_lst[j]):
                    subset = set()
                    for k in range(len(sublst)):
                        subset.add(sublst[k])
                    cnt_lst[j] = cnt_lst[j] + len(subset)
                    break
        else:
            name_lst.append(name)
            subset = set()
            for k in range(len(sublst)):
                subset.add(sublst[k])
            cnt_lst.append(len(subset))
    for i in range(len(name_lst)):
        for j in range(i + 1,len(name_lst)):
            if(cnt_lst[j] > cnt_lst[i]):
                cnt_lst[i],cnt_lst[j] = cnt_lst[j],cnt_lst[i]
                name_lst[i],name_lst[j] = name_lst[j],name_lst[i]
    for i in range(6):
        print(i + 1,name_lst[i])
    print('')
def question9():
    print('Question 9 :')
    global data
    global n
    top3_actor = []
    min_lst = []
    max_lst = []
    dif_lst = []
    for i in range(n):
        name = data[i][3]
        sublst = data[i][4].split('|')
        if(name in top3_actor):
            for j in range(len(top3_actor)):
                if(name == top3_actor[j]):
                    year = int(data[i][5])
                    if(min_lst[j] > year):
                        min_lst[j] = year
                    if(max_lst[j] < year):
                        max_lst[j] = year
                    dif_lst[j] = max_lst[j] - min_lst[j]
                    break
        else:
            top3_actor.append(name)
            min_lst.append(int(data[i][5]))
            max_lst.append(int(data[i][5]))
            dif_lst.append(0)
    cnt = 0
    for i in range(len(top3_actor)):
        for j in range(i + 1,len(top3_actor)):
            if(dif_lst[j] > dif_lst[i]):
                dif_lst[i],dif_lst[j] = dif_lst[j],dif_lst[i]
                top3_actor[i],top3_actor[j] = top3_actor[j],top3_actor[i]
    for i in range(3):
        print(i + 1,top3_actor[i])
    print('')
question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
