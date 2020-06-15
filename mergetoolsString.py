import textwrap
def merge_the_tools(string, k):
    wrapped = textwrap.wrap(string,k)
    fin = []
    for temp in wrapped:
        middle = []
        for i in temp:
            if i not in middle:
                middle.append(i)
        fin.append("".join(middle))
    print("\n".join(fin))
    #can also write as below:
    #unpack the list and separate each element by \n
    #print(*fin,sep ="\n")

    #####Sorter approach
    ############Using ITR and ZIP

S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)