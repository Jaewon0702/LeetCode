Two Sum
=========
# Easy
## Soultion 1 
Run Time: 1788ms  
Beats: 17.20%  
Time Taken: 4m 15s  
Time Compexity: O(N^2)  
  
## Solution 2
Rum Time: 0ms
Beats: 100%
Time Taken: 7m 19s
Time Compexity: O(N)  

'''python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if(compliment in hmap):
                return [hmap[compliment], i]
            hmap[num] = i
        
'''
