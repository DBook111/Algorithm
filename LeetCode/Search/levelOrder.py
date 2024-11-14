# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # 记录当前层, 即深度
        depth = 0
        
        # 初始化一个队列
        queue = deque()
        queue.append((root, depth))
        
        temp = []
        
        while queue:
            # 先出队
            cur_node, cur_depth = queue.popleft()
            # 访问出队元素
            temp.append((cur_node, cur_depth))
            if cur_node.left is not None:
                # 左孩子入队
                queue.append((cur_node.left, cur_depth+1))
            if cur_node.right is not None:
                # 右孩子入队
                queue.append((cur_node.right, cur_depth+1))
        
        # 还原深度信息
        res = []        
        for i in range(len(temp)):
            cur_res = []
            for j in range(len(temp)):
                if temp[j][1] == i:
                    cur_res.append(temp[j][0].val)
            res.append(cur_res)
            
        # filter
        res = [sublist for sublist in res if sublist]
        return res




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
    level_order = [3, 9, 20, None, None, 15, 7]
    root = build_tree(level_order)

    solu = Solution()
    print(solu.levelOrder(root))