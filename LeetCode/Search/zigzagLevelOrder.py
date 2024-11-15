from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        next_level_queue = deque()
        cur_level_queue = deque()
        res = []
        i = 1 # 从奇数开始
        queue.append(root)
        while queue or next_level_queue:                        
            cur_node = queue.popleft()
            cur_level_queue.append(cur_node)
            # 存储下一层的所有节点          
            if cur_node.left:
                next_level_queue.append(cur_node.left)
            if cur_node.right:
                next_level_queue.append(cur_node.right)
            
            if not queue:
                # 当前层全部出完queue, 
                # 如果当前层是奇数，将当前层正序放入cur_res；否则，逆序放入
                cur_res = []
                if i % 2 == 1:
                    while cur_level_queue:
                        cur_res.append(cur_level_queue.popleft().val)
                else:
                    while cur_level_queue:
                        cur_res.append(cur_level_queue.pop().val)
                i += 1
                res.append(cur_res)
                    
                # 将 next_level_queue 中的值都压入 queue 中
                while next_level_queue:
                    queue.append(next_level_queue.popleft())
                
        return res  