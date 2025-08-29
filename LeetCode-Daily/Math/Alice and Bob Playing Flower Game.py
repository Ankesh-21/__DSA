'''
# Leetcode : 3021
# T.C : O(1)
# S.C : O(1)
'''
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
		# T.C : O(n * m)
		# S.C : O(1)
        '''
        # first choose n lane choose by alice
        cnt = 0
        for i in range(1,n+1):
            incr = i % 2
            for j in range(1,m + 1,incr + 1):
                if (i + j) % 2 == 1:
                    cnt += 1
        for i in range(1,m + 1):
            incr = i % 2
            for j in range(1,n + 1,incr + 1):
                if (i + j) % 2:
                    cnt += 1

        return cnt
        '''
        n_even = n // 2
        n_odd = (n + 1) // 2
        m_even = m // 2
        m_odd = (m + 1) // 2

        # as we know odd + even = odd
        return n_even * m_odd + n_odd * m_even
