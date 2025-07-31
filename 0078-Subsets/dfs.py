class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def dfs(start:int):
            if len(current) <= len(nums):
                result.append(current[:])
            for j in range(start, len(nums)):
                if nums[j] not in current:
                    current.append(nums[j])
                    dfs(j+1)
                    current.pop()
        dfs(0)
        return result
        
