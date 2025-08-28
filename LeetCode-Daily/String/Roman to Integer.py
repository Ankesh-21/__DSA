'''
# Leetcode :13
# T.C : O(N)
# S.C : O(M) # M no of possible Romans
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }

        ans = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i + 1 < len(s) and s[i+1] == 'V':
                    ans += romans['IV']
                    i += 1
                elif i + 1 < len(s) and s[i+1] == 'X':
                    ans += romans['IX']
                    i += 1
                else:
                    ans += romans[s[i]]
            elif s[i] == 'X':
                if i+ 1 < len(s) and s[i+1] == 'L':
                    ans += romans['XL']
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'C':
                    ans += romans['XC']
                    i += 1
                else:
                    ans += romans[s[i]]
            elif s[i] == 'C':
                if i+1 < len(s) and s[i+1] == 'D':
                    ans += romans['CD']
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'M':
                    ans += romans['CM']
                    i += 1
                else:
                    ans += romans[s[i]]
            else:
                ans += romans[s[i]]
            i += 1
        return ans