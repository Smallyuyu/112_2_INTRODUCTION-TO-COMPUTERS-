#2D array
board = [['-'] * 7 for i in range(6)]
#input 3
x,y,k = map(int,input('Enter index x,y,k (seperated by whitespace): ').split())
#input to list
lst = list(map(int,input().split()))
#dict
mp = {'a':1}
del mp['a']
mp.get('a')
key = list(mp.keys())
value = list(mp.values())
for key,value in mp:
    print(key,value)
#tuple
t = (2,2,2)
#set
s = {1,2,3}
#random
items = [1,2,3,4]
random.shuffle(items)
print(random.randint(1,10)) #1-10的隨機整數
print(random.uniform(1.1,5.4)) #1.1-5.4的隨機浮點數
