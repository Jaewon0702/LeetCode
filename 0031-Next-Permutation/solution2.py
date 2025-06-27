lass Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing index from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2: Find the next larger number to swap with nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

        # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
            
         # Step 4: Reverse the subarray from i+1 to endAdd commentMore actions
        left, right = i+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
