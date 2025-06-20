Remove nth Node from end of the lists
=========
# Median
Run Time: 0ms      
Beats: 100%      
Time Taken: 5m 23s      
Time Compexity: O(N)

## How is it working?
To point the nth node from the end of the list, I have to use two pointers: fast and slow  
1. Move fast for n
2. Move both fast and slow until it points the end(l - n)(The length of the node is l)
3. Move slow for l-n(This is the nth node from the end of the list)
EX) fast: n + (l-n)
slow: l-n

## How to remove(skip) a node
``` python
slow.next = slow.next.next
```
This means that "Hey node 3, instead of pointing to node 4, now point to node 5!"


