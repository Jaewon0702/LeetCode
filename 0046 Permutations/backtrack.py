class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def bfs():
            if len(nums) == len(current):
                result.append(current[:])
            for j in range(len(nums)):
                if nums[j] not in current:
                    current.append(nums[j])
                    bfs()
                    current.pop()
        bfs()
        return result
