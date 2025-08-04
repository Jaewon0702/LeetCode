
Word search
=========
# Medium
Run Time: 3151 ms         
Beats: 82.09%       
Time Taken: 31m 24s  
Time Compexity: O(K * 3^L), where K ≤ N
Space Complexity : O(N)    

## What's diffrent between these codes?
```python
for i in range(rows):
    for j in range(cols):
        if board[i][j] == word[0]:  # ✅ Check first letter match
            if dfs(i, j, 0):
                return True

```
```python
for r in range(rows):
    for c in range(cols):
        if dfs(r, c, 0):
            return True

```

| Version      | Time Complexity | Notes                                                     |
| ------------ | --------------- | --------------------------------------------------------- |
| **Original** | `O(N * 3^L)`    | Starts DFS from all `N` cells                             |
| **This one** | `O(K * 3^L)`    | Only starts from `K` cells where `board[i][j] == word[0]` |


So:

If word[0] is rare in the board → much faster  

If word[0] appears in many cells → about the same as before    
 
✅ This is a real-world performance win without changing worst-case complexity.   

