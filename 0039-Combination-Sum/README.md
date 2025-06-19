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




