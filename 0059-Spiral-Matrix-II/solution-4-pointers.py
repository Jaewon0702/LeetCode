class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = left = 0
        bot = right = n - 1
        num = 1
        result = [[0]*n for _ in range(n)]
        # Don't use this code: result = [[0]*3]*3-> Shallow copy
        while left <= right and top <= bot:
            # Traverse left to right
            for col in range(left, right+1):
                result[top][col] = num
                num += 1
            top +=1
            # Traverse top to bottom
            for row in range(top,bot + 1):
                result[row][right] = num
                num += 1
            right -=1

            # Traverse right to left
            for col in range(right,left-1,-1):
                result[bot][col] = num
                num += 1
            bot -= 1
            
            # Traverse bot to top
            for row in range(bot, top - 1, -1):
                result[row][left] = num
                num += 1
            left += 1
        return result
