from collections import deque

class Graph():
    def __init__(self,v):
        self.v = v + 1
        self.adj = {i:[] for i in range(self.v)}
    def addEdges(self,u,v):
        self.adj[u].append(v)
    def topoSort(self,adj,indegree,topo):
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            topo.append(node)
            for el in adj[node]:
                indegree[el] -= 1
                if indegree[el] == 0:
                    q.append(el)
        if len(topo) == self.v:
            return False
        return True

if __name__ == '__main__':
    g = Graph(10)
    g.addEdges(0,4)
    g.addEdges(7,4)
    g.addEdges(6,4)
    g.addEdges(1,4)
    g.addEdges(4,9)
    g.addEdges(9,1)
    g.addEdges(2,8)
    g.addEdges(5,8)
    topo = []
    indegree = [0 for _ in range(g.v)]
    for i in range(g.v):
        for node in g.adj[i]:
            indegree[node] += 1
    # print(indegree)
    if g.topoSort(g.adj,indegree,topo):
        print('Cyclic Graph')
    else:
        print('Acyclic Graph')
    