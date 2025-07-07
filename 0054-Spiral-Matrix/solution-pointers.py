class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top = left = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # Traverse left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse top to bottom
            for row in range(top,bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # Traverse right to left
                for col in range(right,left-1,-1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                #Traverse left to right
                for row in range(bottom,top-1,-1):
                    result.append(matrix[row][left])
                left += 1
        return result
