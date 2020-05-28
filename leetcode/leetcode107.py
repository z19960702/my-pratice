from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def preorder(node: TreeNode,deep : int):  # 先序遍历
            if node is None:
                return 
            deep += 1
            if len(res) < deep:
                res.append([node.val])
            else :
                res[deep-1].append(node.val)
            preorder(node.left,deep)
            preorder(node.right,deep)
        preorder(root,0)
        return res[::-1]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(3)
Solution().levelOrderBottom(root)