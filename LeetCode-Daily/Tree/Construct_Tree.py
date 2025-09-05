import sys
import math

sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

class TreeNode:
	def __init__(self,val = None):
		self.val = val;
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = TreeNode()
	def insertNode(self,val):
		node = TreeNode(val)
		ptr = self.root
		if ptr.val == None:
			self.root = node
			return
		prev = None
		while ptr:
			if (node.val < ptr.val):
				prev = ptr
				ptr = ptr.left
			else:
				prev = ptr
				ptr = ptr.right

		if prev.val < node.val:
			prev.right = node
		else:
			prev.left = node
	def inorder(self,root):
		if root == None:
			# print('null',end = ' ')
			return None
		self.inorder(root.left)
		print(root.val,end = ' ')
		self.inorder(root.right)

	def preorder(self,root):
		if root == None:
			print('null',end = ' ')
			return None
		print(root.val,end = ' ')
		self.preorder(root.left)
		self.preorder(root.right)
def solve():

	T = Tree()
	# root created e.g T.root

	T.insertNode(5)
	T.insertNode(1)
	T.insertNode(6)
	T.insertNode(7)
	T.insertNode(8)

	T.preorder(T.root)

tc = 1
tc = int(input())
for _ in range(tc):
	solve()