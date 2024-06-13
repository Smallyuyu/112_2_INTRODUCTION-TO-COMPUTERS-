#H24121133 統計一 陳星宇
s = str(input('Enter a string: '))
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
print('Longest palindrome substring is : ',ansstr)
print('Length is: ',anslen)
