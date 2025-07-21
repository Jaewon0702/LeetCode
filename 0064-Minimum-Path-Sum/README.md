Minimum Path Sum
=========
# Median
Run Time: 0 ms              
Beats: 100%      
Time Taken: 27m 37s    
Time Compexity: O(m*n)

## List Comprehension
```python
row, col = len(grid), len(grid[0])
dp = [[0 for _ in range(col)] for _ in range(row)]
```

This is deep copy. Each elememts can be modified independently!    

``` python
row, col = len(grid), len(grid[0])
dp = [[0]*col]*row
```
This is shallow copy! Don't do this...   
