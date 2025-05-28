class Graph:
    def __init__(self,v):
        self.v = v+1
        self.adj = {i:[] for i in range(self.v)}
    def addEdges(self,u,v):
        self.adj[u].append(v)
    def visul(self):
        print(self.adj)

    def DFS(self,visited,src,stack):
        visited[src] = True
        for node in self.adj[src]:
            if not visited[node]:
                self.DFS(visited,node,stack)
        stack.append(src)
if __name__ == '__main__':
    G = Graph(6)
    G.addEdges(0,3)
    G.addEdges(0,2)
    G.addEdges(2,3)
    G.addEdges(3,1)
    G.addEdges(2,1)
    G.addEdges(1,4)
    G.addEdges(5,4)
    G.addEdges(5,1)

    stack = []
    visited = [False for _ in range(6)]
    for i in range(6):
        if not visited[i]:
            G.DFS(visited,i,stack)
    stack.reverse()
    print(stack)