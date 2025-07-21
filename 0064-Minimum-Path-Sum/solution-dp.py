class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return grid[0][0]
        
        # Generate empty list with List Comprehension
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = grid[0][0]
        # Fill the top row
        for j in range(1, col):
           dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the left column
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of dp
        for i in range(1, row):
            for j in range(1,col):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                
        return dp[row-1][col-1]
