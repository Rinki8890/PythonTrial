#import queue
#from pip._vendor.urllib3.util import queue

#global queue
def cache(q):
    queue = []
    for i in q:
        value = int(i[1])
        if i[0] == 'get':
            get(value,queue)
        else:
            put(value,queue)
    return queue
def get(value,queue):    
    if value in queue:
        queue.remove(value)
        queue.insert(0,value)
    else:
        put(value,queue)
    return queue
def put(value,queue):
    if len(queue) < 3:
        queue.insert(0,value)
    else:
        if value not in queue:
            queue.pop(2)
            queue.insert(0,value)
    return queue

if __name__ == "__main__":
    q = []
    for _ in range(5):
        o = input().split()
        q.append(o)
    print(cache(q))