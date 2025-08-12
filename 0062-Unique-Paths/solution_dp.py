class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for r in range(m):
            for c in range(n):
                if c > 0:
                    dp[c] += dp[c-1]
        return dp[-1]
        
