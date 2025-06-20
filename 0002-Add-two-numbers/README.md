
Add Two numbers
=========
# Median
## Soultion
Run Time: 3ms      
Beats: 72.83%      
Time Taken: 30m 30s      
Time Compexity: O(Max(N,M))    

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

```

## Why carry is needed?
The carry variable plays a crucial role in simulating how addition works digit by digit, especially when the sum of two digits exceeds 9.   
For exampe, if total = 6 + 4 + 0 >= 10  
carry = 1, and you have to **carry over** the extra to the next digit — just like in normal arithmetic!
