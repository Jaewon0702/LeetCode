
Remove duplicates from sorted array
=========
# Easy
## Soultion
Run Time: 0ms      
Beats: 100%      
Time Taken: 17m 30s      
Time Compexity: O(N)

### What is the role of i?
i is the pointer for the place to insert the next unique number!   

### Trial and error
First time, I tried this code   
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(set(nums))
        return len(nums)
```

But I failed, because set() does not preserve order, so if order matters (which it often does), this breaks the requirement.

Review 2
