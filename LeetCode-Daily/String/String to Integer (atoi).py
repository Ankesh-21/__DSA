'''
# LeetCode : 8
# T.C : O(N)
# S.C : O(1)
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        digits = '0123456789'
        ans = ''
        # removing white space
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # adding sign
        if i < len(s) and s[i] == '-':
            ans += '-'
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        #integer 
        while i < len(s) and s[i] in digits:
            ans += s[i]
            i += 1
        
        # if ans size 1 and it contains no digits just discard
        if len(ans) == 1 and ans[0] not in digits:
            ans = ""
        if ans == "":
            ans = '0'
        
        # Rounding
        if (int)(ans) < (-2**31):
            ans = (-2 ** 31)
        if (int)(ans) > (2 ** 31 - 1):
            ans = (2 ** 31 - 1)
        return (int)(ans)