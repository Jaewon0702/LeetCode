class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first = nums.index(target)
            second = len(nums) - nums[::-1].index(target) - 1
            return [first, second]
        except:
            return [-1, -1]
