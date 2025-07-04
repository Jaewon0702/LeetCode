class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = currentNum = nums[0]
        for n in nums[1:]:
            currentNum = max(n,currentNum + n)
            maxNum = max(maxNum, currentNum)
        return maxNum
