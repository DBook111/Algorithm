class Node:
    def __init__(self, val: int, next: None, random: None):
        self.val = int(val)
        self.next = next
        self.random = random
    
    # def copyRandomlist(self, head: 'Node') -> 'Node':
    #     cur = head
    #     dum = pre = Node(0)
    #     while cur:
    #         node = Node(cur.val) # 复制节点
    #         pre.next = node      # 新链表的 前驱节点 -> 当前节点
    #         # pre.random = '???'
    #         cur = cur.next
    #         pre = node
    #     return dum.next
    
    # 方法一：哈希表
    # 利用哈希表的查询特点，考虑构建 原链表节点 和 新链表节点 的键值对映射关系，再遍历构建新链表各节点的 next 和 random 引用指向
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]            
        