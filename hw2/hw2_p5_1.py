#H24121133 統計一 陳星宇
def f(x):
    a = 0
    b = 1
    for i in range(0,x - 1):
        a, b = b, a + b
    return b
        
n = int(input('Input an integer number: '))
print('The ',n,' th Fibonacci sequence number is: ',f(n))
