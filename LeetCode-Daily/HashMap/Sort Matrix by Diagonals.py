'''
# Leetcode : 3446
# T.C : O(N * M)
# S.C : O(N * M)
'''
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = [[0 for _ in range(m)]for _ in range(n)]
        d = {k:[] for k in range(n + m)}
        # managing upper triangle first
        for i in range(n):
            for j in range(m):
                if (i < j):
                    d[abs(i - j)].append(grid[i][j])
        
        for key,li in d.items():
            d[key].sort(reverse = True)
        # print(d)
        for i in range(n):
            for j in range(m):
                if i < j:
                    ans[i][j] = d[abs(i - j)][-1]
                    d[abs(i - j)].pop()
        d = {k:[] for k in range(n + m)}
        # for lower triangle
        for i in range(n):
            for j in range(m):
                if (i >= j):
                    d[abs(i - j)].append(grid[i][j])
        for key,li in d.items():
            d[key].sort()
        for i in range(n):
            for j in range(m):
                if i >= j:
                    ans[i][j] = d[abs(i - j)][-1]
                    d[abs(i - j)].pop()
        return ans
