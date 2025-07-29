'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def Preorder(self,root):
        if root == None:
            return
        print(root.data)
        self.Preorder(root.left)
        self.Preorder(root.right)
                
    def buildTree(self, inorder, preorder):
        # code here
        # a global index that track the preorder traversal
        self.preorder_idx = 0

        # a mapping of inorder value for constant time searching

        self.d = {val:idx for idx,val in enumerate(inorder)}

        def build(start,end):
            if start > end:
                return None

            # getting next value for constructing the tree
            preorder_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            # position of that value from inorder

            inorder_idx = self.d[preorder_val]

            root = Node(preorder_val)

            root.left = build(start,inorder_idx - 1)
            root.right = build(inorder_idx + 1,end)
            
            return root
        return build(0,len(inorder) - 1)