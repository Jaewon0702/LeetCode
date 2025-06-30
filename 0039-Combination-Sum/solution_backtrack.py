class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        result = []
        def DFS(i: int, total: int):
            if total == target:
                result.append(current[:])
                return
            elif total < target:
                for j in range(i, len(candidates)):
                    current.append(candidates[j])
                    DFS(j,total + candidates[j])
                    current.pop() 
        DFS(0,0)
        return result
