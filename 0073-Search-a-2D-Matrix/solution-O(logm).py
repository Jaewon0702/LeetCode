class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            mid_val = matrix[row][col]
            if target == mid_val:
                return True
            elif target < mid_val: 
                high = mid - 1
            else: 
                low = mid + 1
        return False

            
        
