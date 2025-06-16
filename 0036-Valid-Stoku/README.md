Valid Stoku
=========
# Median
Run Time: 3ms        
Beats: 82.36%      
Time Taken: 20m 5s      
Time Compexity: O(1)

## What happen with this code?

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        rows = [set() for _ in range(size)]
# rows[set(),set(),set(),set(),set(),set(),set(),set(),set()]
```

```python
box_index = (r // 3) * 3 + (c // 3)
```
box_index =   
000 111 222 000 111 222 000 111 222     
333 444 555 333 444 555 333 444 555...     
666 777 888 666 777 888 666 777 888   
