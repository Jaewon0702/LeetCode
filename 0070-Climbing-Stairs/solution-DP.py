class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        if n <= 2:
            return n
        for i in range(2, n):
            steps.append(steps[i-1] + steps[i-2])
        return steps[-1]     
