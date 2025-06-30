class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added = str(int(''.join(map(str,digits))) + 1)
        return [int(s) for s in added]
