#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    contact = []
    for i in queries:
        if i[0] == 'add':
            contact.append(i[1])
            word = ' '.join(contact)
        elif i[0]== "find":
            count=0
            for w in word.split():
                if w.find(i[1]) != -1:
                    count+=1
            yield count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
