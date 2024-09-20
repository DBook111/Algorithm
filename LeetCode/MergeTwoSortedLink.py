# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        res = cur = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                cur = list2
                list2 = list2.next
            else:
                cur.next = list1
                cur = list1
                list1 = list1.next
        if list1 != None:
            while list1:
                cur.next = list1
                cur = list1
                list1 = list1.next
        elif list2 != None:
            while list2:
                cur.next = list2
                cur = list2
                list2 = list2.next
        return res.next
        