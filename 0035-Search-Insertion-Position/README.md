Search Insertion Position
=========
# Easy
## Soultion-Binary Search
Run Time: 0ms        
Beats: 100%      
Time Taken: 11m 17s      
Time Compexity: O(Log N)

## What's difference beteween this codes?  
This is the accepted answer  
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            # left side is sorted
            if target <= nums[mid]:
                if nums[left] < target <= nums[mid]:
                    left += 1
                else:
                    right -= 1
            else:
                if nums[mid] <= target < nums[right]:
                    right -= 1
                else:
                    left += 1
        return left

```
This is the unaccepted code:  
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            # left side is sorted
            if target <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    left += 1
                else:
                    right -= 1
            else:
                if nums[mid] < target <= nums[right]:
                    right -= 1
                else:
                    left += 1
        return left
```
