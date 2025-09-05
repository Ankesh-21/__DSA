class DSU:
	def __init__()
class Graph:
	def __init__(self,v):
		self.V = v
		# self.E = e
		self.adj = [[]for _ in range(self.V)]
	def insertEdges(self,u,v):
		self.adj[u].append(v)
		self.adj[v].append(u)

G = Graph(3)

G.insertEdges(0,1)
G.insertEdges(1,2)
G.insertEdges(2,0)

print(G.adj)
		