'''
@ Leetcode : 230
@ Time Complexity : O(h) where h is the height of the tree
@ Space Complexity : O(1) where h is the height of the tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [-1]
        cnt = k
        def solve(root):
            nonlocal cnt
            if root == None:
                return
            solve(root.left)
            cnt -= 1
            if cnt == 0:
                ans[0] = root.val
                return 
            solve(root.right)
        solve(root)
        return ans[0]
        