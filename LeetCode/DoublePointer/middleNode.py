from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        cur = head
        length = 1
        while True:
            if cur.next != None:
                cur = cur.next
                length += 1
            else:
                break
        if length % 2 == 1:
            cur2 = ListNode()
            cur2 = head
            for i in range(int(length/2)):
                cur2 = cur2.next
        else:
            cur2 = ListNode()
            cur2 = head
            for i in range(int(length/2)):
                cur2 = cur2.next
        return cur2