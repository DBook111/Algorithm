# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root
                    
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
    level_order = [3,5,1,6,2,0,8,None,None,7,4]
    root = build_tree(level_order)

    solu = Solution()
    print(solu.lowestCommonAncestor(root, TreeNode(5), TreeNode(4)))