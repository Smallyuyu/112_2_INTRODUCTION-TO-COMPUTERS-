#H24121133 統計一 陳星宇
year = int(input("Please input Year: "))
month = int(input("Please input Month: "))
week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
def getweek(y,m,d): #算第幾天
    if(m == 1 or m == 2):
        y -= 1
        m +=12
    return (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7;
def leapyear(y): #算潤年
    if(y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
        return 1
    else:
        return 0
def printf(d):
    if(d < 10):
        print('0' + str(d),end = '  ')
    else:
        print(d,end = '  ')
#main
m_to_d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if(month == 2 and leapyear(year)):
    m_to_d[2] = 29
curd = 1
curw = int(getweek(year,month,1)) + 1
print(curw)
#輸出
for s in week:
    print(s,end = ' ')
print(' ',end = '\n')
for i in range(0,curw):
    print('    ',end = '')
while(curd <= m_to_d[month]):
    printf(curd)
    if(int(curw) % 7 == 6):
        print(' ',end = '\n')
    curd += 1
    curw += 1
