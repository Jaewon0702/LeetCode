import itertools
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1) # How to use recursive function
        result = ""

        for digit,group in itertools.groupby(str(prev)):
            count = len(list(group))
            result += str(count) + digit
        return result
            
        


        
