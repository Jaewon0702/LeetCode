from itertools import combinations_with_replacement
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for i in range(1, target // min(candidates) + 1):
            for combi in combinations_with_replacement(candidates, i):
                if sum(combi) == target:
                    result.append(list(combi))
        return result
