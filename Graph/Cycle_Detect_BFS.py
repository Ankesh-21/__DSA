import sys
import queue

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

class Graph:
	def __init__(self,v):
		self.v = v + 1
		self.adj = {i:[] for i in range(self.v)}

	def addEdges(self,u,v):
		self.adj[u].append(v)
		self.adj[v].append(u)

	def visul(self):
		print(self.adj)

	def BFS(self,visited,src,parent):

		q= queue.Queue()
		q.put((src,parent))

		while not q.empty():
			node,par = q.get()
			for el in self.adj[node]:
				if el == par:
					continue
				if not visited[el]:
					visited[el] = True
					q.put((el,node))
				else:
					return True
		return False


	def isCyclic(self):
		visited = [False] * self.v
		parent = -1

		for i in range(self.v):
			if not visited[i] and self.BFS(visited,i,parent):
				print('Graph is Cyclic')
				return
		print('Graph is not Cyclic')

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