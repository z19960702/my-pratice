class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1,  t2) :
            if (t1 == None and t2 == None) :
                return True
            if (t1 == None or t2 == None):
                 return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left)  and isMirror(t1.left, t2.right);
        return isMirror(root,root)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print (Solution().isSymmetric(root))