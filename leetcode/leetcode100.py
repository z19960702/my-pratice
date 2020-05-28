# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(node):  # 先序遍历
            if node is None:
                return [None]
            result = [node.val]
            left_item = preorder(node.left)
            right_item = preorder(node.right)
            return result + left_item + right_item
        res1 = preorder(p)
        res2 = preorder(q)
        print (res1,res2)
        return True if res1 == res2 else False

root = TreeNode(1)
root.left = TreeNode(3)
#root.right = TreeNode(3)

root1 = TreeNode(1)
#root1.left = TreeNode(2)
root1.right = TreeNode(3)
print (Solution().isSameTree(root,root1))