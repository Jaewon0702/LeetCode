def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            low = 0
            high = len(matrix[0]) - 1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    return True
                elif target < nums[mid]: 
                    high = mid - 1
                else: 
                    low = mid + 1
        return False
