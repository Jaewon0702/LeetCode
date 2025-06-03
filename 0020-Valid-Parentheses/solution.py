class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            elif bracket in bracket_map:
                if not stack or stack[-1] != bracket_map[bracket]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
        
