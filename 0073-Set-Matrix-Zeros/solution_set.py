class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows,zero_cols  = set(), set()
         
        for m in range(rows):
            for n in range(cols):
                if matrix[m][n] == 0:
                    zero_rows.add(m)
                    zero_cols.add(n)
        # Make row 0
        for r in zero_rows:
            for c in range(cols):
                matrix[r][c] = 0
        
        # Make cols 0
        for r in range(rows):
            for c in zero_cols:
                matrix[r][c] = 0
