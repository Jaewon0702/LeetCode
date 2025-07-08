lass Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        current = intervals[0]
        for inter in intervals[1:]:
            if current[1] >= inter[0]:
                current[1] = max(current[1], inter[1])
            else:
                result.append(current)
                current = inter
        result.append(current)
        return result
