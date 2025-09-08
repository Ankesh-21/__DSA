class Node:
    def __init__(self,val:int = 0):
        self.val = val
        self.left = None
        self.right = None
def insertNode(values,ind):
    root = None
    if ind < len(values) and values[ind] != 'N':
        root =  Node(values[ind])
        root.left = insertNode(values,2 * ind + 1)
        root.right = insertNode(values,2 * ind + 2)

    return root
def maintainCost(root,cost):
    if root == None:
        return 0
    print(root.val)
    leftPart = root.val + maintainCost(root.left,cost)
    rightPart = root.val + maintainCost(root.right,cost)

    if leftPart > cost:
        print(f'leftPart= {leftPart}')
        root.left = None
        leftPart = 0
    if rightPart > cost:
        print(f'rightPart= {rightPart}')
        root.right = None
        rightPart = 0
    
    if leftPart == 0 and rightPart == 0:
        return root.val
    return leftPart if leftPart != 0 else rightPart

def traverse(root):
    if root == None:
        return
    print(root.val,end = ' ')
    traverse(root.left)
    traverse(root.right)
    
def solve():
    nodeVal = [1,4,8,5,6,2,1,7,'N','N','N','N','N',2,'N']
    root = insertNode(nodeVal,0)
    traverse(root)
    print()
    maintainCost(root,11)
    # traverse(root)
if __name__ == '__main__':
    solve()
# main()