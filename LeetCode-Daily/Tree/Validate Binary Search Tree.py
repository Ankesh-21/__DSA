'''
@ Given the root of a binary tree, determine if it is a valid binary search tree (BST).
@ Leetcode : 98
@ Time Complexity : O(n)
@ Space Complexity : O(h) where h is the height of the tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,lb,ub):
            if root:
                if root.val > lb and root.val < ub:
                    return isValid(root.left,lb,root.val) and isValid(root.right,root.val,ub)
                else:
                    return False
            else:
                return True
        return isValid(root,(int)(-2 ** 32), (int)(2 ** 32))