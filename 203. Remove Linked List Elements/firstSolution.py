# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        cur = head
        #newHead = head

        while cur.next:
            if head.val == val:
               cur = head.next
               head = head.next
               continue
            elif cur.next.val == val:
                cur.next = cur.next.next
                cur = cur.next
            else:
                cur = cur.next
        
        return head