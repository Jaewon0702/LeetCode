class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        results = [""]

        for digit in digits:
            next_result = []
            for combo in results:
                for letter in mapping[digit]:
                    next_result.append(combo + letter)
            results = next_result
        return results
        
