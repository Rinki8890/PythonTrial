from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        print('************',self.graph)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        queue = []
        queue.append(s)

        visited = [False]*len(self.graph)
        print(len(self.graph))
        if len(self.graph) > 1:
            visited[s] = True
       
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)   

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 

  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 