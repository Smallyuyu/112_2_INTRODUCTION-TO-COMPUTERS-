#input
sa = float(input('Enter the shopping amount: '))
m = str(input('Enter the membership level (Regular or Gold): '))
#判斷
if(m == 'Regular'):
    if(sa >= 3000):
        sa = sa * 0.8
    elif(sa >= 2000):
        sa = sa * 0.85
    elif(sa >= 1000):
        sa = sa * 0.9
    print(m,' $',sa,sep ='')
elif(m == 'Gold'):
    if(sa >= 3000):
        sa = sa * 0.75
    elif(sa >= 2000):
        sa = sa * 0.8
    elif(sa >= 1000):
        sa = sa * 0.85
    print(m,' $',sa,sep ='')
else:
    print('Invalid membership level. Please enter \'Regular\' or \'Gold\'.')
