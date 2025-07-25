# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length, tail = 1, head
        # Move tail to last index and get length of ListNode!
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        # Move to the pivot and rotate
        cur = head
        for i in range(length-k-1):
            cur = cur.next
        Newhead = cur.next
        cur.next = None
        tail.next = head
        return Newhead
