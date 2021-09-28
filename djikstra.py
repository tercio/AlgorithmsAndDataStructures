from collections import defaultdict
import sys
from queue import Empty, PriorityQueue

class Graph:
    def __init__(self):
        self.G = defaultdict(list)


    def __str__(self):
        text = "Graph: %d vertices\n" % (len(self.G))
        for node in self.G.keys():
           text += "[node: %s] -> %s\n" % (node,self.G[node])

        return text 

    def addEdge(self,u,v,d):
        self.G[u].append((v,d))


    def shortestPath (self,u):
        dist = [sys.maxsize] * (len(self.G) + 1) 
        dist[u] = 0
        pq = []
        import heapq
        heapq.heappush(pq,(0,u))
        prev = {}

        while pq:
            u = heapq.heappop(pq)[1]
            for vd in self.G[u]:
                v = vd[0]
                d = vd[1]

                du = dist[u]
                if dist[v] > du + d:
                    dist[v] = du+d
                    heapq.heappush(pq,(dist[v],v))
                    prev[v] = u

        #self.printSolution(dist)
        return dist,prev


    def printSolution(self,dist):

        for node in self.G.keys():
            print (node,"   :   ",dist[node])

"""
      [1]  -1- [3]
   1 /             \1
[0]                 [5]
   2 \             /2
      [2]  -2-  [4]

"""
g = Graph()
g.addEdge(0,1,1)
g.addEdge(0,2,2)
#g.addEdge(0,5,1)
g.addEdge(2,4,2)
g.addEdge(1,3,1)
g.addEdge(3,5,1)
g.addEdge(4,5,2)

print (g)
d,p = g.shortestPath(0)
print (d)
g.printSolution(d)

target = 5
print ("Caminho para o node %d: " % (target))

def printPath(p,target):
    if target in p:
        printPath(p,p[target])
    else:
        return

    print (p[target],end="-> ")
    
printPath(p,target)


