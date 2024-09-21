from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        root_left = left_cur = ListNode()
        left_cur = root_left
        root_right = right_cur = ListNode()
        right_cur = root_right
        cur = cur_next = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                cur_next = cur.next
                left_cur.next = cur
                cur.next = None
                left_cur = cur
            else:
                cur_next = cur.next
                right_cur.next = cur
                cur.next = None
                right_cur = cur
            cur = cur_next
        left_cur.next = root_right.next
        return root_left.next