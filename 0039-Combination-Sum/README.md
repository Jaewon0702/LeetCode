Combination Sum
=========
# Median
Run Time: 8ms        
Beats: 69.39%      
Time Taken: 20m 36s      
Time Compexity: O(Len(Candidates)(Target/Min(Candidates)))  
## Wrong Solution
``` python
from itertools import combinations_with_replacement
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for i in range(1, target // min(candidates) + 1):
            for combi in combinations_with_replacement(candidates, i):
                if sum(combi) == target:
                    result.append(list(combi))
        return result
```
It works for a candidates list which has short length, but does not work with long length!   
Ex) candidates = [8,10,9,32,25,27,22,38,15,5,3,26,30,11,21,36,37] (X)   
candidates = [4, 5, 6, 7] (O)  

There are some reasons:   
1. Generates all combinations of a fixed size i, even those that greatly exceed target.

2. Checks each combination with sum(combi) == target, which is inefficient (O(k) time for each combination).

3. combinations_with_replacement produces a massive number of permutations if target is large and candidates are small

## Backtrack Solution
``` python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        result = []
        def DFS(i: int, total: int):
            if total == target:
                result.append(current[:])
                return
            elif total < target:
                for j in range(i, len(candidates)):
                    current.append(candidates[j])
                    DFS(j,total + candidates[j])
                    current.pop() 
        DFS(0,0)
        return result
```
### Why make a copy (current[:])?
Without copy, result holds a reference to the changing current list.  
For example,   
```python
current = [2,3,4,5]
result = []
result.append(current[:])
current.pop()
result
```
result: [[2, 3, 4, 5]]  
``` python
current = [2,3,4,5]
result = []
result.append(current)
current.pop()
result
```
result: [[2, 3, 4]] 

### What current.pop() does in backtracking
The key is: pop() allows you to cleanly remove the last added number, so your current list is ready for the next candidate at that level of recursion.  







