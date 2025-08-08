Spiral Matrix II
=========
# Median
Run Time: 0 ms              
Beats: 100%      
Time Taken: 34m 44s    
Time Compexity: O(N^2) 

### Shallow copy Vs. Deep copy
When you make an empty list, you must be careful!     
Shallow copy   
```python
result = [[0]*3]*3
```
This creates a shallow copy — all rows in result actually point to the same list. So when you update one row, all rows are updated, which is not what you want.    

Deep copy
```python
result = [[0]*n for _ in range(n)]
```
Use a list comprehension to make independent rows.   
Each row is now its own list in memory.  
