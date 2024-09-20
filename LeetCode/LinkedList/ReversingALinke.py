# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = temp = ListNode()
        cur = head
        if head == None:
            return head
        while cur.next:
            cur = cur.next
        
        while head != cur:
            temp = head
            head = head.next
            if cur.next == None:
                temp.next = None
                cur.next = temp
            else:
                temp.next = cur.next
                cur.next = temp
        
        return head
        
            
            