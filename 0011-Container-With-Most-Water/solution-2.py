class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        sizes = []
        while left <= right:
            size = (right -left) * min(height[left], height[right])
            sizes.append(size)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(sizes)
        

