from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # dummy helps handle edge cases cleanly
        fast = slow = dummy

        # Move fast n+1 steps ahead to maintain a gap of n between slow and fast
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return dummy.next
