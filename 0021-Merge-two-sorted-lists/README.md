Merge Two Sorted Lists
=========
# Easy
## Soultion
Run Time: 0ms      
Beats: 100%      
Time Taken: 30m 30s      
Time Compexity: O(N + M)    

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # Add a value from the list
                list1 = list1.next # move pointer to next value in the list
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # append remaing data from list1 or list2
        current.next = list1 if list1 else list2
        return dummy.next
```
### Why need dummy?
```python
dummy = ListNode()
current = dummy
```
1. **dummy** is a placeholder node - it does not hold meaningful data.   
2. It acts as the starting point of your new likned list.   
3. current is a pointer used to build the new list starting from dummy.
4. **dummy.next** points the whole data of the new linked list!

### How it works?
list1 = 1 -> 2 -> 4   
list2 = 1 -> 3 -> 4   
Compare first node between list1 and list2 and append a smaller one to current!    
current = 1 -> 1 -> 2...  

