Permutations II
=========
# Median
Run Time: 0 ms              
Beats: 100%      
Time Taken: 17m 19s    
Time Compexity: O(N! * N)
## Correct Approach: Backtrack + Used array
- A used list to track if nums[i] is already in current
- A way to skip duplicates only when a duplicate would generate the same subtree
``` python
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue

```
Skips the same number in the same level tree to prevents duplicates!    
