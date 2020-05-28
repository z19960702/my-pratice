class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDeep = 0 
        def preorder(node: TreeNode,deep : int):  # 先序遍历
            
            if node is None:
                return 
            deep += 1
            if(deep > self.maxDeep):
                self.maxDeep = deep
            print (self.maxDeep)
            preorder(node.left,deep)
            preorder(node.right,deep)
        preorder(root,0)
        print (self.maxDeep)
        return self.maxDeep

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(3)
print (Solution().maxDepth(root))