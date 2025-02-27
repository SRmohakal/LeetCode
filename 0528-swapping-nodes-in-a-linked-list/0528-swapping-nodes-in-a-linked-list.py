# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_k=last_k=head
        
        for _ in range(k-1):
            first_k=first_k.next
        
        runner=first_k
        while runner.next:
            runner=runner.next
            last_k=last_k.next
        
        first_k.val,last_k.val=last_k.val,first_k.val

        return head