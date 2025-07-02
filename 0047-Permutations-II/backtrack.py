class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []
        used = [False] * len(nums)
        def bfs():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                current.append(nums[i])
                bfs()
                current.pop()
                used[i] = False
        bfs()
        return result 
        
