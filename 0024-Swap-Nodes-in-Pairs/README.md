Swap Nodes in Pairs
=========
# Median
## Soultion
Run Time: 0ms      
Beats: 100%      
Time Taken: 23m 40s      
Time Compexity: O(N)

### What is this code?
```python
dummy = ListNode(0,head)
```
- 0 is the value of the dummy node (doesn’t really matter — we ignore it).  

- head is the actual input linked list.  

- So the dummy node points to the head.
```scss
dummy(0) → 1 → 2 → 3

```

### The Process of swapping
You have to reorganize the whole Linked Nodes!  
Before Swap:  
``` ini
prev  = dummy
first = head = 1
second = head.next = 2

```
Visualization
``` sql
prev → 1 → 2 → 3 → 4
         ↑    ↑
       first second

```
Swap steps:
``` python
prev.next = second     # dummy → 2
first.next = second.next  # 1 → 3
second.next = first    # 2 → 1

```
Update prev to first, and head to first.next:
``` bash
dummy → 2 → 1 → 3 → 4
               ↑
              head

```

I reviewed once
