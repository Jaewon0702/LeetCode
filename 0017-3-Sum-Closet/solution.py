class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = float('inf') # positive infinite
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
        #If this is closer to the target than our current best, update
                if abs(closet-target) > abs(total- target):
                    closet = total

                if total == target: return total
                elif(total < target): left += 1
                else: right -= 1
        return closet

        
