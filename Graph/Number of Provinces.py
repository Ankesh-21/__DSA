def DFS(adj,visited,src):
    visited[src] = True
    for node in adj[src]:
        if not visited[node]:
            DFS(adj,visited,node)
    

class Solution:
    def findCircleNum(self, isconnected: List[List[int]]) -> int:
        adj = {i:[] for i in range(201)}
        n = len(isconnected)
        for i in range(n):
            for j in range(n):
                if isconnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False for _ in range(n+1)]
        cnt = 0
        for i in range(n):
            if not visited[i]:
                DFS(adj,visited,i)
                cnt += 1
        return cnt