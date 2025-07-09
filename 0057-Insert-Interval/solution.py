class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort()
        current = intervals[0]
        for inter in intervals[1:]:
            if current[1] < inter[0]:
                result.append(current)
                current = inter
            else:
                current[1] = max(inter[1], current[1])
        result.append(current)
        return result
