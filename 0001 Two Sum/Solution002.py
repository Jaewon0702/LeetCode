class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if(compliment in hmap):
                return [hmap[compliment], i]
            hmap[num] = i
        
