# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    # 中序遍历
    def in_order(self, root, res):
        if not root:
            return
        self.in_order(root.left, res)
        res.append(root.val)
        self.in_order(root.right, res)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.in_order(root, res)
        # 当前，res 中保存的是顺序的
        return res[k-1]
            
        

if __name__ == '__main__':
    # 构建二叉树
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(level_order):
        if not level_order:
            return None

        root = TreeNode(level_order[0])
        queue = [root]
        i = 1

        while i < len(level_order):
            node = queue.pop(0)

            if level_order[i] is not None:
                node.left = TreeNode(level_order[i])
                queue.append(node.left)
            i += 1

            if i < len(level_order) and level_order[i] is not None:
                node.right = TreeNode(level_order[i])
                queue.append(node.right)
            i += 1

        return root

    # 输入层序遍历数组
    level_order = [5,3,6,2,4,None,None,1]
    root = build_tree(level_order)

    solu = Solution()
    print(solu.kthSmallest(root, 3))