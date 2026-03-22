# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        temp = ListNode(0)
        while head:
            prev = temp
            while prev.next and prev.next.val < head.val: prev = prev.next
            head.next, prev.next, head = prev.next, head, head.next
        return temp.next

        