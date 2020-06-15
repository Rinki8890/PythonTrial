# Enter your code here. Read input from STDIN. Print output to STDOUT
#Input String
#love
#velo low vole lovee volvell lowly lower lover levo loved love lovee lowe lowes lovey lowan lowa evolve loves volvelle lowed love
s = input().strip()
words = input().split()
count = 0
#all the ltters of s
# for all the ltters of words in words

for word in words:
    flag = False
    for i in s:
        if i in word:
            flag = True
        else:
            flag = False
            break
    if flag:
        for j in word:
            if j in s:
                flag = True
            else:
                flag = False
        if flag:
            count += 1

print(count)

            




