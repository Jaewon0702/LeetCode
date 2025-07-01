Combination Sum II
=========
# Median
Run Time: 33 ms              
Beats: 15.25%      
Time Taken: 16m 30s    
Time Compexity:    
### How to avoid duplicates  
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        candidates.sort()
        def DFS(start: int, total: int):
            if current in result: ## To avoid duplicate combinations
                return
            if total == target:
                result.append(current[:])
                return
            elif total < target:
                for j in range(start, len(candidates)):
                    if j > start and candidates[j] == candidates[j - 1]:
                        continue
                    current.append(candidates[j])
                    DFS(j+1, total + candidates[j])
                    current.pop()
        DFS(0,0)
        return result
```
I used this code:  
```python
if j > start and candidates[j] == candidates[j - 1]:
    continue
```
If I don't use this code, it causes a time exceed error with this example:  
candidates= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  
target = 30  

  
