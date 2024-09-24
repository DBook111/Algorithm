class Node:
    def __init__(self, val: int, next: None, random: None):
        self.val = int(val)
        self.next = next
        self.random = random
    
    def copyRandomlist(self, head: 'Node') -> 'Node':
        cur = head
        dum = pre = Node(0)
        while cur:
            node = Node(cur.val) # 复制节点
            pre.next = node      # 新链表的 前驱节点 -> 当前节点
            # pre.random = '???'
            cur = cur.next
            pre = node
        return dum.next
        
        