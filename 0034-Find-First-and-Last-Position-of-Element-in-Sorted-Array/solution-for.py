class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                break
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] == target:
                result.append(j)
                break
        if len(result) == 0:
            return [-1, -1]
        elif len(result) == 1:
            result = result * 2
        return result
