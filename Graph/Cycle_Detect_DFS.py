import math

class Graph:
    def __init__(self,v):
        self.v = v+1
        self.adj = {i:[] for i in range(self.v)}
    def addEdges(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def visul(self):
        print(self.adj)

    def DFS(self,visited,parent,u):
        visited[u] = True
        print(u)
        for el in self.adj[u]:
            if parent == el:
                continue
            if not visited[el]:
                if self.DFS(visited,u,el):
                    return True
            else:
                return True
        return False
    def isCyclic(self):
        visited = [False for i in range(self.v)]
        parent = -1
        for i in range(self.v):
            if not visited[i] :
                if self.DFS(visited,parent,i):
                    print('Graph is Cyclic')
                    return
        print('Graph is not Cyclic')
        return

if __name__ == '__main__':
    G = Graph(7)
    G.addEdges(1,2)
    G.addEdges(1,3)
    G.addEdges(2,5)
    G.addEdges(3,6)
    G.addEdges(5,7)
    G.addEdges(6,7)
    G.addEdges(3,4)
    G.visul()
    # G.addEdges(0,1)

    G.isCyclic()