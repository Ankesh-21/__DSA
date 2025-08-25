class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        d = {i:[] for i in range(n + m + 1)}
        for i in range(n):
            for j in range(m):
                d[i + j].append(mat[i][j])
        ans = []
        # to sort the dictionary on basis of key
        d_sorted = {k: v for k, v in sorted(d.items(), key=lambda x: x[0])}
        # print(d_sorted)
        for key,List in d_sorted.items():
            if key % 2 == 0:
                for i in range(len(List) -1 ,-1, -1):
                    ans.append(List[i])
            else:
                for el in List:
                    ans.append(el)
        return ans

