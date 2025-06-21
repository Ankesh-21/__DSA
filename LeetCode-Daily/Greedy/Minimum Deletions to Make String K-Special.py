'''
* LeetCode - 3085
* T.C : O(26 * 26)
* S.C : O(26)
'''
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = [0 for _ in range(26)]
        for ch in word:
            d[ord(ch) - ord('a')] += 1
        
        mini = float('inf')
        for i in range(len(d)):
            cnt = 0
            for j in range(len(d)):
                if d[j] < d[i]:
                    cnt += d[j]
                elif d[j] > (d[i] + k):
                    cnt += (d[j] - d[i] - k)
            mini = min(mini,cnt)
        return mini
            
