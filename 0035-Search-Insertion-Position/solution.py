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


            
        
