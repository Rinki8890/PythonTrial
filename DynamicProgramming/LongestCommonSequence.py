def LCS(s1, s2):
    x = len(s1)-1
    y = len(s2)-1
    #outer loops are row, inner loops are columns
    matrix = [[0 for _ in range(len(s1)+1)]for _ in range(len(s2)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix[x][y]


def commonChild(s1, s2):
    matrix=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s1)-1,-1,-1):
            if s1[i]==s2[j]:
                matrix[i][j]=1+matrix[i+1][j+1]
            else:
                matrix[i][j]=max(matrix[i+1][j],matrix[i][j+1])

    return(matrix[0][0])


#################most correct version

def fit(a,b):
    return 1 if a==b else 0

def common_child(a,b):
    length = len(a)
    result = [fit(a[0],b[0])]
    for i in range(1,length):
        result.append(max(result[-1], fit(a[0],b[i])))
    for i in range(1,length):
        tmp = result[0]
        result[0] = fit(a[i],b[0])
        for j in range(1, length):
            tmp2 = result[j]
            result[j] = max(result[j-1], result[j], tmp + fit(a[i],b[j]))
            tmp = tmp2
    return result[-1]

a = input()
b = input()
a = [ord(i)-65 for i in a]
b = [ord(i)-65 for i in b]
print (common_child(a,b))


############Editorial

def LCS(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in xrange(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]


if __name__ == '__main__':
    a = raw_input()
    b = raw_input()

    print LCS(a, b)