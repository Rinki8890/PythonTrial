import string

N = int(input())
Q = int(input())
s = ''
res = mid = '' 
j = 0
for i in range(N):
  s += string.ascii_letters[i+26]
print('Your string is', s)
  
for i in range(Q):
    if j >= len(s)-1:
      if j == len(s)-1:
        mid = "?"+s[j]
        j = j-len(s)
      else:
        j = j-len(s)
        mid = '?'+s[j]
      print(mid+s[j+1])
    else:
      print("?"+s[j]+s[j+1])
    inpu = input().strip()
    if inpu == '>':
      res += s[j+1]
    elif inpu == '<':
      res += s[j+1] 
    j += 1
    if len(res) == N:
      break
print(res)