class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        start, end = 0,-1
        current = intervals[0]
        for i in range(len(intervals)):
            if current[end] >= intervals[i][start]:
                current[-1] = max(current[-1],intervals[i][end])
            else:
                result.append(current)
                current = intervals[i]
        result.append(current)
        return result
