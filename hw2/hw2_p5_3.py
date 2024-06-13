#H24121133 統計一 陳星宇
#費氏數列
def f(x):
    a = 0
    b = 1
    for i in range(0,x - 1):
        a, b = b, a + b
    return b
#迴文
def pal(s):
    n = len(s)
    anslen = 0
    ansstr = s[0]
    for i in range(0,n):
        #奇數len
        left = i
        right = i
        while(left >= 0 and right < n and s[left] == s[right]):
            left -= 1
            right += 1
        left += 1
        right -= 1
        if(right - left + 1 > anslen):
            anslen = right - left + 1
            ansstr = s[left:right + 1]
        #偶數len
        left = i - 1
        right = i
        while(left >= 0 and right < n and s[left] == s[right]):
            left -= 1
            right += 1
        left += 1
        right -= 1
        if(right - left + 1 > anslen):
            anslen = right - left + 1
            ansstr = s[left:right + 1]
    return anslen,ansstr
#加密
def ascii(s,k,a,b):
    return chr(((((ord(s) + k) * a + b) - 65) % 26) + 65)
#input
n = int(input('The number of the requested element in Fibonacci (n) = '))
s1 = str(input('The first string for Palindromic detection (s1) = '))
s2 = str(input('The second string for Palindromic detection (s2) = '))
pt = str(input('The plaintext to be encrypted: '))
print('----- extract key for encypt method -----')
s1len,s1str = pal(s1)
s2len,s2str = pal(s2)
print('The ',n,'-th Fibonacci sequence number is: ',f(n))
print('Longest palindrome substring within first string is: ',s1str)
print('Length is: ',s1len)
print('Longest palindrome substring within first string is: ',s2str)
print('Length is: ',s2len)
print('----- encryption completed -----')
#main
for i in range(0,len(pt)):
      print(ascii(pt[i],f(n),s1len,s2len),end = '')
