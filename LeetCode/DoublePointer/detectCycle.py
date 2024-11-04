from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针问题
        # fast, slow = ListNode(0), ListNode(0)
        fast, slow = head, head
        while True:            
            if not (fast and fast.next):
                return  
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
    
    
class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
