'''
* Leetcode : 125
* T.C : O(N)
* S.C : O(1)
'''
def check(ch):
    nums = "1234567890"
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ch in nums or ch in chars

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while not check(s[i]) and i < j:
                i += 1
            while not check(s[j]) and j > i:
                j -= 1 
            ch_left = s[i].lower()
            ch_right = s[j].lower()

            print(ch_left,ch_right)

            if ch_left != ch_right:
                return False
            
            i += 1
            j -= 1
        return True