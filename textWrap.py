import textwrap

def wrap(string, max_width):
    l = []
    for i in range(0,len(string),max_width):
        l.append(string[i:i+max_width])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    #method to wrap text is textwrap.wrap that returns a list
    #check this module for more details
    #https://docs.python.org/3/library/textwrap.html
    print(textwrap.wrap(string,max_width))